import streamlit as st
from ui_components.upload_pdf import handle_pdf_upload
from ui_components.search_interface import handle_paper_search
from llm_modules.report_generator import generate_final_report

st.set_page_config(page_title="LLM 논문 요약 리포트", layout="wide")

# --- Sidebar ---
st.sidebar.title("📘 논문 입력 옵션")
input_method = st.sidebar.radio("논문 입력 방식 선택", ["PDF 업로드", "논문 검색 (arXiv)"])

# --- Main Title ---
st.title("🧠 LLM 기반 논문 요약 및 시각화 리포트")

# --- 논문 입력 처리 ---
paper_data = None
if input_method == "PDF 업로드":
    paper_data = handle_pdf_upload()
elif input_method == "논문 검색 (arXiv)":
    paper_data = handle_paper_search()

# --- 결과 처리 및 출력 ---
if paper_data:
    with st.spinner("요약 및 시각화 리포트를 생성 중입니다..."):
        report_sections = generate_final_report(paper_data)

    # 요약 출력
    st.subheader("🔍 요약 결과")
    st.markdown(report_sections['summary'])

    # 시각화 출력
    st.subheader("📊 시각화 및 표 해석")
    for chart in report_sections['visualizations']:
        st.image(chart, use_column_width=True)

    # 전체 리포트 다운로드
    st.subheader("📄 리포트 다운로드")
    st.download_button("HTML로 저장", data=report_sections['html'], file_name="report.html", mime="text/html")
