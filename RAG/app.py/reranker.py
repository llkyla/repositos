"""
reranker.py

Re-scores the candidate chunks returned by hybrid retrieval using a more
precise (and more expensive) relevance model. This is the stage that
typically yields the largest accuracy improvement for the smallest amount
of implementation effort, since the reranker only needs to score a small
candidate set (e.g. 50) instead of the whole corpus.

In production, replace `LexicalOverlapReranker` with a real cross-encoder,
for example:

    from sentence_transformers import CrossEncoder
    model = CrossEncoder("Dongjin-kr/ko-reranker")
    scores = model.predict([(query, chunk.text) for chunk in candidates])

This module keeps a dependency-free lexical-overlap scorer so the pipeline
is runnable end-to-end without network access, while defining the same
interface (`CrossEncoderReranker`) you would use with a real model.
"""

from abc import ABC, abstractmethod
from typing import List, Tuple

from chunking import Chunk
from hybrid_retrieval import tokenize


class BaseReranker(ABC):
    """Common interface so the retrieval pipeline can swap rerankers freely."""

    @abstractmethod
    def rerank(self, query: str, candidates: List[Chunk], top_k: int = 5) -> List[Chunk]:
        ...


class LexicalOverlapReranker(BaseReranker):
    """Placeholder reranker based on token overlap (Jaccard-style score).

    This is a stand-in for a real cross-encoder model. It is intentionally
    simple: it only looks at exact token overlap between the query and each
    candidate chunk, with no notion of semantic similarity or word order.
    """

    def _score(self, query: str, doc_text: str) -> float:
        q_tokens = set(tokenize(query))
        d_tokens = set(tokenize(doc_text))
        if not q_tokens:
            return 0.0
        overlap = len(q_tokens & d_tokens)
        return overlap / len(q_tokens)

    def rerank(self, query: str, candidates: List[Chunk], top_k: int = 5) -> List[Chunk]:
        scored: List[Tuple[Chunk, float]] = [
            (c, self._score(query, c.text)) for c in candidates
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [c for c, _score in scored[:top_k]]


class CrossEncoderReranker(BaseReranker):
    """Production-shaped reranker wrapping a real cross-encoder model.

    Example model:
        model_name = "Dongjin-kr/ko-reranker"  # Korean cross-encoder
        or "cross-encoder/ms-marco-MiniLM-L-6-v2" for English.

    This class is written against the sentence-transformers CrossEncoder
    API. It is not instantiated by default in this repo because the
    execution environment used to build this file has no network access
    to download model weights; wire it up in your own environment.
    """

    def __init__(self, model_name: str = "Dongjin-kr/ko-reranker"):
        try:
            from sentence_transformers import CrossEncoder
        except ImportError as exc:
            raise ImportError(
                "sentence-transformers is required for CrossEncoderReranker. "
                "Install it with `pip install sentence-transformers`."
            ) from exc
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, candidates: List[Chunk], top_k: int = 5) -> List[Chunk]:
        pairs = [(query, c.text) for c in candidates]
        scores = self.model.predict(pairs)
        scored = list(zip(candidates, scores))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [c for c, _score in scored[:top_k]]


def flag_conflicting_definitions(candidates: List[Chunk]) -> List[str]:
    """Governance helper: detect when reranked chunks come from documents
    with different `updated_at` metadata but overlapping subject matter.

    This supports the "standard vs. actual usage mismatch" detection
    described in the project README. It is a lightweight heuristic, not a
    semantic conflict detector: it flags when top candidates disagree on
    last-updated dates, which is a proxy for potential version drift.
    """
    dates = {
        c.metadata.get("updated_at")
        for c in candidates
        if c.metadata.get("updated_at")
    }
    warnings = []
    if len(dates) > 1:
        warnings.append(
            f"Multiple document versions found among top results: {sorted(dates)}. "
            "Verify which version is authoritative before relying on this answer."
        )
    return warnings


if __name__ == "__main__":
    from chunking import chunk_text
    from hybrid_retrieval import BM25Retriever, DenseRetriever, HybridRetriever

    doc = (
        "API naming rules are as follows. All REST API endpoints must use "
        "lowercase letters and hyphens. Master data standard defines the "
        "customer ID as a 12-digit string. This standard applies to both "
        "the CRM system and the ERP system. The data governance committee "
        "audits standard compliance quarterly."
    )
    chunks = chunk_text(
        doc, doc_id="it_policy_001", chunk_size=120, overlap_ratio=0.15,
        metadata={"updated_at": "2025-03-01"},
    )

    retriever = HybridRetriever(BM25Retriever(), DenseRetriever()).fit(chunks)
    candidates = retriever.search("customer ID master data standard", top_k=4)

    reranker = LexicalOverlapReranker()
    top_results = reranker.rerank("customer ID master data standard", candidates, top_k=2)

    for c in top_results:
        print(c.chunk_id, "|", c.text)

    warnings = flag_conflicting_definitions(top_results)
    print("Governance warnings:", warnings)