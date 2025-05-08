import streamlit as st
from llm_modules.paper_search import search_arxiv

def handle_paper_search() -> dict:
    query = st.text_input("논문 키워드를 입력하세요:")
    if query:
        with st.spinner("논문 검색 중..."):
            result = search_arxiv(query)
            st.code(result[:1000], language='xml')  # 향후 요약 적용
            return {"text": result}
    return None
