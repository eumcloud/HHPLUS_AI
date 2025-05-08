import streamlit as st
import pdfplumber

def extract_text_from_pdf(uploaded_file) -> str:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
    return full_text

def handle_pdf_upload() -> dict:
    uploaded_file = st.file_uploader("논문 PDF 파일을 업로드하세요", type=["pdf"])
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        return {"text": text, "file_path": uploaded_file}
    return None
