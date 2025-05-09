import streamlit as st
from ui_components.upload_pdf import handle_pdf_upload
from llm_modules.report_generator import generate_final_report

st.set_page_config(page_title="논문 요약 리포트", layout="wide")

st.title("📄 논문 PDF 요약")

uploaded_pdf = handle_pdf_upload()  # PDF 업로드 기능 사용
if uploaded_pdf:
    with st.spinner("요약 생성 중..."):
        report = generate_final_report(uploaded_pdf)

    st.subheader("요약 결과")
    st.markdown(report["summary"])

    st.subheader("리포트 다운로드")
    st.download_button(
        label="HTML 리포트 저장",
        data=report["html"],
        file_name="report.html",
        mime="text/html"
    )
