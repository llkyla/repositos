"""
chunking.py

Splits raw documents (IT policy docs, technical standards, master data
definitions) into overlapping, sentence-aware chunks suitable for embedding
and indexing. Structured master data records are converted into natural
language sentences upstream so they can flow through this same pipeline.
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Chunk:
    """A single retrievable unit of text with traceability metadata."""
    text: str
    doc_id: str
    chunk_id: str
    metadata: dict = field(default_factory=dict)


def split_into_sentences(text: str) -> List[str]:
    """Naive sentence splitter based on punctuation boundaries.

    For production use with Korean/English mixed corpora, consider
    swapping this for a proper sentence tokenizer (e.g. kss for Korean,
    or spaCy/nltk for English) to handle abbreviations and edge cases.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sentences if s.strip()]


def chunk_text(
    text: str,
    doc_id: str,
    chunk_size: int = 800,
    overlap_ratio: float = 0.15,
    metadata: Optional[dict] = None,
) -> List[Chunk]:
    """Chunk a document into overlapping windows without splitting sentences.

    Args:
        text: Full document text.
        doc_id: Stable identifier for the source document.
        chunk_size: Target chunk size in characters (500-1000 is a common
            starting point for policy/standards documents).
        overlap_ratio: Fraction of the previous chunk carried into the next
            one, to preserve context across chunk boundaries.
        metadata: Extra fields attached to every chunk (title, department,
            version, last_updated_at, source_url, etc.). This metadata is
            what enables filtering and governance checks downstream.

    Returns:
        List of Chunk objects ready for embedding.
    """
    metadata = metadata or {}
    sentences = split_into_sentences(text)
    chunks: List[Chunk] = []
    current = ""
    chunk_idx = 0
    overlap_chars = int(chunk_size * overlap_ratio)

    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= chunk_size:
            current = (current + " " + sentence).strip()
            continue

        if current:
            chunks.append(
                Chunk(
                    text=current,
                    doc_id=doc_id,
                    chunk_id=f"{doc_id}_{chunk_idx}",
                    metadata=metadata.copy(),
                )
            )
            chunk_idx += 1
            # Carry a tail of the previous chunk forward to preserve context.
            tail = current[-overlap_chars:] if overlap_chars > 0 else ""
            current = (tail + " " + sentence).strip()
        else:
            # Single sentence longer than chunk_size: keep it as its own chunk.
            current = sentence

    if current:
        chunks.append(
            Chunk(
                text=current,
                doc_id=doc_id,
                chunk_id=f"{doc_id}_{chunk_idx}",
                metadata=metadata.copy(),
            )
        )

    return chunks


def structured_record_to_text(record: dict, schema_hint: str = "") -> str:
    """Convert a structured master data record into a natural language
    sentence so it can be embedded alongside unstructured policy text.

    Example:
        {"field": "customer_id", "definition": "12-digit string",
         "owner": "CRM Team", "updated_at": "2025-03-01"}
        ->
        "Field 'customer_id' is defined as '12-digit string'. Owned by
         CRM Team. Last updated on 2025-03-01."
    """
    parts = []
    if "field" in record:
        parts.append(f"Field '{record['field']}'")
    if "definition" in record:
        parts.append(f"is defined as '{record['definition']}'")
    if "owner" in record:
        parts.append(f"Owned by {record['owner']}")
    if "updated_at" in record:
        parts.append(f"Last updated on {record['updated_at']}")

    sentence = ". ".join(p for p in parts if p)
    if schema_hint:
        sentence = f"[{schema_hint}] {sentence}"
    return sentence + "." if sentence and not sentence.endswith(".") else sentence


if __name__ == "__main__":
    sample_policy = (
        "API naming rules are as follows. All REST API endpoints must use "
        "lowercase letters and hyphens. For example, the path should follow "
        "the /user-profile format. Version information must be included in "
        "the URL path, using /v1/, /v2/ conventions. This rule was revised "
        "in March 2025."
    )

    result = chunk_text(
        sample_policy,
        doc_id="it_policy_001",
        chunk_size=150,
        overlap_ratio=0.15,
        metadata={"title": "API Naming Rules", "dept": "IT Strategy Team"},
    )

    for c in result:
        print(c.chunk_id, "|", len(c.text), "chars |", c.text)