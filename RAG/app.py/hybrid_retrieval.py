"""
hybrid_retrieval.py

Combines dense (embedding-based) retrieval with sparse (BM25 keyword-based)
retrieval, then fuses both rankings with Reciprocal Rank Fusion (RRF).

This matters for enterprise document QA because internal docs often contain
exact codes, system names, and acronyms (e.g. "CRM-2024-v3") that dense
embeddings alone tend to under-match, while pure keyword search misses
paraphrased questions. Combining both improves recall.

In production, replace:
  - DenseRetriever's `_embed` method with a real embedding model
    (e.g. sentence-transformers, OpenAI embeddings, or a Hugging Face model).
  - The in-memory vector store with FAISS, Chroma, or a managed vector DB.
  - BM25Retriever with the `rank_bm25` package if you prefer not to
    maintain a custom implementation.
"""

import math
import re
from collections import Counter, defaultdict
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

from chunking import Chunk


def tokenize(text: str) -> List[str]:
    """Basic tokenizer: lowercases and strips punctuation.

    For Korean text, consider a proper morphological tokenizer
    (e.g. KoNLPy, Mecab) for better keyword matching quality.
    """
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return [t for t in text.split() if t]


class BM25Retriever:
    """Minimal BM25 implementation (Okapi BM25) for sparse keyword retrieval."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.doc_freqs: List[Counter] = []
        self.idf: Dict[str, float] = {}
        self.doc_lens: List[int] = []
        self.avgdl: float = 0.0
        self.corpus_size: int = 0
        self.chunks: List[Chunk] = []

    def fit(self, chunks: List[Chunk]) -> "BM25Retriever":
        self.chunks = chunks
        tokenized_docs = [tokenize(c.text) for c in chunks]
        self.corpus_size = len(chunks)
        self.doc_lens = [len(d) for d in tokenized_docs]
        self.avgdl = sum(self.doc_lens) / max(self.corpus_size, 1)

        df: Dict[str, int] = defaultdict(int)
        for doc in tokenized_docs:
            self.doc_freqs.append(Counter(doc))
            for term in set(doc):
                df[term] += 1

        for term, freq in df.items():
            self.idf[term] = math.log(
                1 + (self.corpus_size - freq + 0.5) / (freq + 0.5)
            )
        return self

    def search(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        """Returns a list of (chunk_id, score) sorted by relevance."""
        query_terms = tokenize(query)
        scores = np.zeros(self.corpus_size)

        for i, freqs in enumerate(self.doc_freqs):
            doc_len = self.doc_lens[i]
            for term in query_terms:
                if term not in freqs:
                    continue
                idf = self.idf.get(term, 0.0)
                tf = freqs[term]
                denom = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                scores[i] += idf * (tf * (self.k1 + 1)) / denom

        ranked_idx = np.argsort(-scores)[:top_k]
        return [(self.chunks[i].chunk_id, float(scores[i])) for i in ranked_idx]


class DenseRetriever:
    """Embedding-based retriever using cosine similarity over a vector index.

    NOTE: `_embed` is a placeholder hashing-based vectorizer so this module
    runs without external dependencies or network access. Swap it out for
    a real embedding model in production, e.g.:

        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("jhgan/ko-sroberta-multitask")
        vector = model.encode(text)
    """

    def __init__(self, embed_fn: Optional[Callable[[str], np.ndarray]] = None,
                 dim: int = 256):
        self.dim = dim
        self.embed_fn = embed_fn or self._hashing_embed
        self.chunks: List[Chunk] = []
        self.vectors: Optional[np.ndarray] = None

    def _hashing_embed(self, text: str) -> np.ndarray:
        """Deterministic bag-of-words hashing embedding (placeholder only)."""
        vec = np.zeros(self.dim)
        for token in tokenize(text):
            idx = hash(token) % self.dim
            vec[idx] += 1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def fit(self, chunks: List[Chunk]) -> "DenseRetriever":
        self.chunks = chunks
        self.vectors = np.vstack([self.embed_fn(c.text) for c in chunks])
        return self

    def search(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        query_vec = self.embed_fn(query)
        # Cosine similarity since vectors are normalized.
        scores = self.vectors @ query_vec
        ranked_idx = np.argsort(-scores)[:top_k]
        return [(self.chunks[i].chunk_id, float(scores[i])) for i in ranked_idx]


def reciprocal_rank_fusion(
    rankings: List[List[Tuple[str, float]]], k: int = 60
) -> List[Tuple[str, float]]:
    """Fuses multiple ranked lists using Reciprocal Rank Fusion.

    RRF only depends on rank position, not raw scores, which makes it
    robust when combining rankings from different scoring scales
    (e.g. BM25 scores vs. cosine similarity).
    """
    fused_scores: Dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, (chunk_id, _score) in enumerate(ranking):
            fused_scores[chunk_id] += 1.0 / (k + rank + 1)

    fused = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    return fused


class HybridRetriever:
    """Combines BM25 and dense retrieval results via RRF."""

    def __init__(self, bm25: BM25Retriever, dense: DenseRetriever):
        self.bm25 = bm25
        self.dense = dense
        self.chunk_lookup: Dict[str, Chunk] = {}

    def fit(self, chunks: List[Chunk]) -> "HybridRetriever":
        self.bm25.fit(chunks)
        self.dense.fit(chunks)
        self.chunk_lookup = {c.chunk_id: c for c in chunks}
        return self

    def search(self, query: str, top_k: int = 10, candidate_pool: int = 50) -> List[Chunk]:
        sparse_results = self.bm25.search(query, top_k=candidate_pool)
        dense_results = self.dense.search(query, top_k=candidate_pool)
        fused = reciprocal_rank_fusion([sparse_results, dense_results])
        top_ids = [chunk_id for chunk_id, _score in fused[:top_k]]
        return [self.chunk_lookup[cid] for cid in top_ids]


if __name__ == "__main__":
    from chunking import chunk_text

    doc = (
        "API naming rules are as follows. All REST API endpoints must use "
        "lowercase letters and hyphens. Master data standard defines the "
        "customer ID as a 12-digit string. This standard applies to both "
        "the CRM system and the ERP system. The data governance committee "
        "audits standard compliance quarterly."
    )
    chunks = chunk_text(doc, doc_id="it_policy_001", chunk_size=120, overlap_ratio=0.15)

    retriever = HybridRetriever(BM25Retriever(), DenseRetriever()).fit(chunks)
    results = retriever.search("customer ID master data standard", top_k=3)

    for c in results:
        print(c.chunk_id, "|", c.text)