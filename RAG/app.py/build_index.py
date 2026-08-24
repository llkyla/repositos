"""
build_index.py

Offline indexing script: loads raw documents and master data records from
disk, chunks them, and fits the hybrid retriever so it is ready to serve
queries. In this reference implementation the "index" is simply the fitted
HybridRetriever object kept in memory / pickled to disk; swap the pickle
step for a real vector DB (FAISS, Chroma, etc.) in production.

Usage:
    python build_index.py --input data/raw_docs --master-data data/master_data
"""

import argparse
import json
import os
import pickle
from typing import List

from chunking import Chunk, chunk_text, structured_record_to_text
from hybrid_retrieval import BM25Retriever, DenseRetriever, HybridRetriever


def load_text_documents(input_dir: str) -> List[dict]:
    """Loads .txt/.md files from a directory. Each file becomes one document.

    Expects an optional sidecar `<filename>.meta.json` file for metadata
    such as title, department, and updated_at. Extend this loader to handle
    PDF/Confluence exports as those sources are onboarded.
    """
    documents = []
    if not os.path.isdir(input_dir):
        return documents

    for filename in sorted(os.listdir(input_dir)):
        if not (filename.endswith(".txt") or filename.endswith(".md")):
            continue

        doc_id = os.path.splitext(filename)[0]
        with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
            text = f.read()

        meta_path = os.path.join(input_dir, f"{doc_id}.meta.json")
        metadata = {}
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)

        documents.append({"doc_id": doc_id, "text": text, "metadata": metadata})

    return documents


def load_master_data_records(master_data_dir: str) -> List[dict]:
    """Loads structured master data definitions from JSON files.

    Expected format per file: a JSON list of records like
        [{"field": "customer_id", "definition": "12-digit string",
          "owner": "CRM Team", "updated_at": "2025-03-01"}, ...]
    """
    records = []
    if not os.path.isdir(master_data_dir):
        return records

    for filename in sorted(os.listdir(master_data_dir)):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(master_data_dir, filename), "r", encoding="utf-8") as f:
            records.extend(json.load(f))

    return records


def build_chunks_from_documents(documents: List[dict]) -> List[Chunk]:
    all_chunks: List[Chunk] = []
    for doc in documents:
        chunks = chunk_text(
            text=doc["text"],
            doc_id=doc["doc_id"],
            chunk_size=800,
            overlap_ratio=0.15,
            metadata=doc.get("metadata", {}),
        )
        all_chunks.extend(chunks)
    return all_chunks


def build_chunks_from_master_data(records: List[dict]) -> List[Chunk]:
    chunks: List[Chunk] = []
    for i, record in enumerate(records):
        sentence = structured_record_to_text(record, schema_hint="MASTER_DATA")
        if not sentence:
            continue
        chunks.append(
            Chunk(
                text=sentence,
                doc_id=f"master_data_{record.get('field', i)}",
                chunk_id=f"master_data_{record.get('field', i)}_0",
                metadata={
                    "title": f"Master Data: {record.get('field', 'unknown')}",
                    "updated_at": record.get("updated_at", "unknown"),
                    "owner": record.get("owner", "unknown"),
                    "length": record.get("length"),
                },
            )
        )
    return chunks


def build_index(input_dir: str, master_data_dir: str, output_path: str) -> HybridRetriever:
    documents = load_text_documents(input_dir)
    records = load_master_data_records(master_data_dir)

    doc_chunks = build_chunks_from_documents(documents)
    master_chunks = build_chunks_from_master_data(records)
    all_chunks = doc_chunks + master_chunks

    print(f"Loaded {len(documents)} documents -> {len(doc_chunks)} chunks")
    print(f"Loaded {len(records)} master data records -> {len(master_chunks)} chunks")
    print(f"Total chunks indexed: {len(all_chunks)}")

    retriever = HybridRetriever(BM25Retriever(), DenseRetriever()).fit(all_chunks)

    with open(output_path, "wb") as f:
        pickle.dump(retriever, f)
    print(f"Index saved to {output_path}")

    return retriever


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the hybrid retrieval index.")
    parser.add_argument("--input", default="data/raw_docs", help="Directory of policy/standard documents.")
    parser.add_argument("--master-data", default="data/master_data", help="Directory of master data JSON files.")
    parser.add_argument("--output", default="index.pkl", help="Path to save the fitted retriever.")
    args = parser.parse_args()

    build_index(args.input, args.master_data, args.output)