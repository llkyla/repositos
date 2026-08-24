"""
governance.py

Master data governance helpers that go beyond simple document QA:
  1. Detect version drift across chunks answering the same question.
  2. Compare a "standard" definition (from a policy document) against an
     "actual" definition (from a live schema / data dictionary export) to
     flag mismatches that data governance teams need to act on.

These functions are designed to be called after retrieval/reranking, right
before generation, so warnings can be injected into the LLM prompt (see
generation.py) and also logged separately for audit purposes.
"""

import re
from dataclasses import dataclass
from typing import Dict, List, Optional

from chunking import Chunk


@dataclass
class GovernanceFinding:
    severity: str  # "info" | "warning" | "critical"
    message: str
    related_chunk_ids: List[str]


def flag_version_drift(chunks: List[Chunk]) -> List[GovernanceFinding]:
    """Flags when top retrieved chunks come from documents with different
    `updated_at` metadata, which is a proxy signal for outdated or
    conflicting policy versions being surfaced together.
    """
    findings: List[GovernanceFinding] = []
    dated_chunks: Dict[str, List[str]] = {}

    for chunk in chunks:
        updated_at = chunk.metadata.get("updated_at")
        if updated_at:
            dated_chunks.setdefault(updated_at, []).append(chunk.chunk_id)

    if len(dated_chunks) > 1:
        findings.append(
            GovernanceFinding(
                severity="warning",
                message=(
                    f"Top results span {len(dated_chunks)} different document "
                    f"versions: {sorted(dated_chunks.keys())}. Confirm which "
                    "version is currently authoritative before relying on this answer."
                ),
                related_chunk_ids=[cid for ids in dated_chunks.values() for cid in ids],
            )
        )
    return findings


def extract_numeric_constraint(text: str) -> Optional[str]:
    """Extracts simple numeric/format constraints from text, e.g. '12-digit
    string' or '8 characters'. Used to compare standard vs. actual schema
    definitions. This is a lightweight regex heuristic, not a full NLP
    parser -- extend it as real document formats are onboarded.
    """
    match = re.search(r"(\d+)[\s-]*(digit|character|char)", text, re.IGNORECASE)
    if match:
        return f"{match.group(1)}-{match.group(2).lower()}"
    return None


def compare_standard_vs_actual(
    standard_chunk: Chunk, actual_schema_record: dict
) -> List[GovernanceFinding]:
    """Compares a policy-defined standard (e.g. 'customer ID is a 12-digit
    string') against an actual schema/data dictionary record (e.g.
    {'field': 'customer_id', 'type': 'VARCHAR(10)'}) and flags mismatches.

    Args:
        standard_chunk: Chunk containing the natural-language policy text.
        actual_schema_record: dict describing the real field definition,
            typically pulled from a live data dictionary or DB catalog,
            e.g. {"field": "customer_id", "length": 10, "type": "VARCHAR"}.
    """
    findings: List[GovernanceFinding] = []

    standard_constraint = extract_numeric_constraint(standard_chunk.text)
    actual_length = actual_schema_record.get("length")

    if standard_constraint and actual_length is not None:
        standard_digits = re.search(r"\d+", standard_constraint)
        if standard_digits and int(standard_digits.group()) != int(actual_length):
            findings.append(
                GovernanceFinding(
                    severity="critical",
                    message=(
                        f"Standard document specifies '{standard_constraint}' for "
                        f"field '{actual_schema_record.get('field', 'unknown')}', but "
                        f"the actual schema defines length={actual_length}. "
                        "This is a master data governance mismatch that should be "
                        "escalated to the data governance committee."
                    ),
                    related_chunk_ids=[standard_chunk.chunk_id],
                )
            )
    return findings


def summarize_findings(findings: List[GovernanceFinding]) -> List[str]:
    """Flattens findings into plain strings for injection into the LLM prompt."""
    return [f"[{f.severity.upper()}] {f.message}" for f in findings]


if __name__ == "__main__":
    standard_doc = Chunk(
        text="Master data standard defines the customer ID as a 12-digit string.",
        doc_id="it_policy_001",
        chunk_id="it_policy_001_1",
        metadata={"title": "Master Data Standard", "updated_at": "2025-03-01"},
    )
    older_doc = Chunk(
        text="Customer identifiers must follow an 8-digit numeric format.",
        doc_id="it_policy_legacy",
        chunk_id="it_policy_legacy_0",
        metadata={"title": "Legacy Data Standard", "updated_at": "2021-06-01"},
    )

    drift_findings = flag_version_drift([standard_doc, older_doc])
    print("Version drift findings:", summarize_findings(drift_findings))

    actual_schema = {"field": "customer_id", "length": 10, "type": "VARCHAR"}
    mismatch_findings = compare_standard_vs_actual(standard_doc, actual_schema)
    print("Schema mismatch findings:", summarize_findings(mismatch_findings))