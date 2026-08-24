"""
app.py

Streamlit entrypoint that ties together retrieval, reranking, governance
checks, and generation into an interactive chatbot UI.

Run with:
    streamlit run app.py

Assumes an index has already been built with build_index.py and saved to
`index.pkl`. If no index is found, falls back to a small in-memory demo
corpus so the app is runnable out of the box.
"""

import os
import pickle

import streamlit as st

from chunking import Chunk, chunk_text
from hybrid_retrieval import BM25Retriever, DenseRetriever, HybridRetriever
from reranker import LexicalOverlapReranker
from governance import flag_version_drift, summarize_findings
from generation import EchoLLMClient, generate_answer


INDEX_PATH = "index.pkl"
TOP_K_CANDIDATES = 20
TOP_K_FINAL = 5


@st.cache_resource
def load_retriever() -> HybridRetriever:
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, "rb") as f:
            return pickle.load(f)

    # Fallback demo corpus so the app runs even without a prebuilt index.
    demo_doc = (
        "API naming rules are as follows. All REST API endpoints must use "
        "lowercase letters and hyphens. Master data standard defines the "
        "customer ID as a 12-digit string. This standard applies to both "
        "the CRM system and the ERP system. The data governance committee "
        "audits standard compliance quarterly."
    )
    demo_chunks = chunk_text(
        demo_doc,
        doc_id="demo_policy",
        chunk_size=150,
        overlap_ratio=0.15,
        metadata={"title": "Demo IT Policy", "updated_at": "2025-03-01"},
    )
    return HybridRetriever(BM25Retriever(), DenseRetriever()).fit(demo_chunks)


def answer_question(query: str, retriever: HybridRetriever) -> dict:
    candidates = retriever.search(query, top_k=TOP_K_CANDIDATES)

    reranker = LexicalOverlapReranker()
    top_chunks = reranker.rerank(query, candidates, top_k=TOP_K_FINAL)

    governance_findings = flag_version_drift(top_chunks)
    warnings = summarize_findings(governance_findings)

    llm_client = EchoLLMClient()  # Swap for a real LLMClient in production.
    result = generate_answer(query, top_chunks, llm_client, warnings=warnings)

    return {
        "answer": result.answer,
        "sources": top_chunks,
        "warnings": warnings,
    }


def main():
    st.set_page_config(page_title="Enterprise Document QA", layout="wide")
    st.title("사내 문서 기반 QA 챗봇")
    st.caption("IT 정책, 기술 표준, 마스터 데이터 정의를 검색해 근거 기반으로 답변합니다.")

    retriever = load_retriever()

    query = st.text_input("질문을 입력하세요", placeholder="예: 고객 ID는 몇 자리 문자열인가요?")

    if st.button("검색") and query:
        with st.spinner("문서를 검색하고 답변을 생성하는 중..."):
            result = answer_question(query, retriever)

        st.subheader("답변")
        st.write(result["answer"])

        if result["warnings"]:
            st.subheader("거버넌스 경고")
            for w in result["warnings"]:
                st.warning(w)

        st.subheader("근거 문서")
        for i, chunk in enumerate(result["sources"], start=1):
            title = chunk.metadata.get("title", chunk.doc_id)
            updated = chunk.metadata.get("updated_at", "unknown")
            with st.expander(f"[Source {i}] {title} (updated: {updated})"):
                st.write(chunk.text)


if __name__ == "__main__":
    main()