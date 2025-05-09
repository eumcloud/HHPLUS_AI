import streamlit as st
import requests
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

# 페이지 설정
st.set_page_config(page_title="논문 요약 API", layout="wide")
st.title("📄 논문 요약 서비스 (Inference API 기반)")

# Hugging Face API Key 로딩
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# API 토큰 체크 (초기 로딩 시간 방지 목적)
if not HF_TOKEN:
    st.error("HF_TOKEN이 설정되지 않았습니다. .env 파일을 확인해주세요.")
    st.stop()

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# UI: 입력 방식 선택
input_method = st.radio("논문 입력 방식 선택", ["📁 PDF 업로드", "🔗 PDF 링크"])
pdf_bytes = None
download_success = False

uploaded_file = None
pdf_url = ""

if input_method == "📁 PDF 업로드":
    uploaded_file = st.file_uploader("논문 PDF 업로드", type=["pdf"])

elif input_method == "🔗 PDF 링크":
    pdf_url = st.text_input("PDF 링크 입력")
    if st.button("PDF 다운로드") and pdf_url.strip():
        try:
            r = requests.get(pdf_url.strip())
            if r.status_code == 200:
                pdf_bytes = r.content
                download_success = True
                st.success("PDF 다운로드 완료")
            else:
                st.error("PDF 다운로드 실패")
        except Exception as e:
            st.error(f"다운로드 오류: {e}")

# 질문 입력
user_question = st.text_input("논문에 대해 궁금한 점을 입력하세요", value="이 논문의 목적과 기여를 요약해줘")

# 요약 버튼 눌렀을 때만 실행 (fitz 포함 로직도 이 때만 실행됨)
if st.button("요약 생성"):
    if input_method == "📁 PDF 업로드" and uploaded_file:
        pdf_bytes = uploaded_file.read()
    elif input_method == "🔗 PDF 링크" and not download_success:
        st.warning("PDF를 먼저 다운로드 해주세요.")
        st.stop()

    if not pdf_bytes:
        st.warning("PDF가 준비되지 않았습니다.")
        st.stop()

    with st.spinner("요약 생성 중..."):
        try:
            # 1. PDF 열기 (지연 가능성 있는 작업 — 버튼 클릭 시에만 실행)
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            full_text = "\n".join([page.get_text() for page in doc])

            # 2. 참고문헌 제거
            lowered = full_text.lower()
            for ref in ["references", "bibliography", "참고문헌", "works cited"]:
                idx = lowered.rfind(ref)
                if idx != -1:
                    full_text = full_text[:idx]
                    break

            # 3. 길이 제한
            trimmed_text = full_text[:1500]

            # 4. 프롬프트 구성
            prompt = f"""
당신은 논문 요약 전문가입니다. 아래 논문 내용을 바탕으로 구조화된 요약을 작성해 주세요:

1. 제목 요약:
2. 연구 목적:
3. 방법론 요약:
4. 주요 실험 결과:
5. 기여 및 의의:
6. 응용 가능성:

추가 질문: {user_question}

논문 내용:
{trimmed_text}
"""

            # 5. Hugging Face API 호출
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 400,
                    "temperature": 0.7,
                },
            }

            response = requests.post(API_URL, headers=HEADERS, json=payload)
            result = response.json()

            if isinstance(result, dict) and "error" in result:
                st.error(f"API 오류: {result['error']}")
            else:
                output = result[0]["generated_text"]
                st.subheader("요약 결과")
                st.markdown(output)

        except Exception as e:
            st.error(f"요약 처리 중 오류 발생: {e}")
