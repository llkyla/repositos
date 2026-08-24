"""
generation.py

Builds the final prompt from retrieved/reranked chunks and calls an LLM to
produce a grounded answer with inline source citations. Also wires in the
governance warnings produced by reranker.flag_conflicting_definitions so
that version-drift risks surface directly in the chatbot's answer.

The LLM call itself is abstracted behind `LLMClient` so you can plug in
OpenAI, an internally hosted model, or any other provider without touching
the prompt-construction logic.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

from chunking import Chunk


SYSTEM_INSTRUCTIONS = (
    "You are an internal IT policy assistant. Answer the question using ONLY "
    "the sources provided below. Cite each claim with its source number in "
    "square brackets, e.g. [Source 1]. If the sources do not contain enough "
    "information to answer confidently, say so explicitly instead of "
    "guessing or relying on outside knowledge."
)


@dataclass
class GeneratedAnswer:
    answer: str
    prompt: str
    used_chunk_ids: List[str]
    warnings: List[str]


class LLMClient(ABC):
    """Abstract interface so any LLM provider can be swapped in."""

    @abstractmethod
    def complete(self, prompt: str) -> str:
        ...


class EchoLLMClient(LLMClient):
    """Offline stand-in LLM client for testing the pipeline without network
    access or API keys. Returns a naive extractive answer instead of a real
    generation, purely so the rest of the pipeline is runnable end-to-end.

    Replace with a real client in production, e.g.:

        class OpenAIClient(LLMClient):
            def __init__(self, model="gpt-4o-mini"):
                from openai import OpenAI
                self.client = OpenAI()
                self.model = model

            def complete(self, prompt: str) -> str:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.choices[0].message.content
    """

    def complete(self, prompt: str) -> str:
        return (
            "[EchoLLMClient placeholder] No real LLM is configured. "
            "Wire up an LLMClient implementation (OpenAI, internal model, "
            "etc.) in generation.py to produce real answers."
        )


def build_context_block(chunks: List[Chunk]) -> str:
    """Formats retrieved chunks into numbered, citable source blocks."""
    blocks = []
    for i, chunk in enumerate(chunks, start=1):
        title = chunk.metadata.get("title", chunk.doc_id)
        updated = chunk.metadata.get("updated_at", "unknown")
        blocks.append(
            f"[Source {i}] (doc: {title}, updated: {updated})\n{chunk.text}"
        )
    return "\n\n".join(blocks)


def build_prompt(query: str, chunks: List[Chunk], warnings: Optional[List[str]] = None) -> str:
    context = build_context_block(chunks)
    warning_block = ""
    if warnings:
        warning_block = "\n\nGOVERNANCE WARNINGS:\n" + "\n".join(f"- {w}" for w in warnings)

    return f"""{SYSTEM_INSTRUCTIONS}

SOURCES:
{context}
{warning_block}

QUESTION: {query}

ANSWER:"""


def generate_answer(
    query: str,
    chunks: List[Chunk],
    llm_client: LLMClient,
    warnings: Optional[List[str]] = None,
) -> GeneratedAnswer:
    """Runs the final generation step and packages the result with metadata
    needed for traceability (which chunks were used, which warnings fired).
    """
    prompt = build_prompt(query, chunks, warnings)
    answer_text = llm_client.complete(prompt)

    return GeneratedAnswer(
        answer=answer_text,
        prompt=prompt,
        used_chunk_ids=[c.chunk_id for c in chunks],
        warnings=warnings or [],
    )


if __name__ == "__main__":
    sample_chunks = [
        Chunk(
            text="Master data standard defines the customer ID as a 12-digit string.",
            doc_id="it_policy_001",
            chunk_id="it_policy_001_1",
            metadata={"title": "Master Data Standard", "updated_at": "2025-03-01"},
        ),
        Chunk(
            text="This standard applies to both the CRM system and the ERP system.",
            doc_id="it_policy_001",
            chunk_id="it_policy_001_2",
            metadata={"title": "Master Data Standard", "updated_at": "2025-03-01"},
        ),
    ]

    result = generate_answer(
        query="What is the format of the customer ID?",
        chunks=sample_chunks,
        llm_client=EchoLLMClient(),
    )

    print("PROMPT:\n", result.prompt)
    print("\nANSWER:\n", result.answer)
    print("\nUSED CHUNKS:", result.used_chunk_ids)