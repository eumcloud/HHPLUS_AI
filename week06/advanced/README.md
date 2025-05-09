 
---

## 📄 논문 요약 LLM 서비스

LLM을 활용한 구조화된 논문 요약 서비스입니다.
사용자가 논문 PDF를 업로드하면, SFT 기반 LLM(Pegasus)을 통해 논문 내용을 다음과 같은 형식으로 요약합니다:

```
1. 제목 요약:  
2. 연구 목적:  
3. 방법론 요약:  
4. 주요 실험 결과:  
5. 기여 및 의의:  
6. 응용 가능성:  
```

---

## 🚀 데모

Streamlit 인터페이스를 통해 손쉽게 PDF 업로드 및 요약 결과 확인 가능.

![streamlit-demo](./demo_screenshot.png)

---

## ✅ 기능 요약

* PDF 업로드 또는 URL 입력
* 논문 텍스트 자동 추출 (PyMuPDF 사용)
* 참고문헌 제거 전처리 포함
* Pegasus 모델 기반 논문 요약
* 구조화된 요약 항목 출력

---

## 🧠 사용 모델

* [`google/pegasus-arxiv`](https://huggingface.co/google/pegasus-arxiv)
* 논문 요약(SFT) 용도로 학습된 공개 모델

---

## 🛠️ 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

> `requirements.txt` 예시:

```text
streamlit
transformers
torch
pymupdf
sentencepiece
python-dotenv
```

### 2. 실행

```bash
streamlit run app.py
```

---

## 📁 프로젝트 구조

```
.
├── app.py               # Streamlit 메인 앱
├── README.md
├── requirements.txt
└── .env                 # (선택) 환경 변수 파일
```

---

## 📌 주의사항

* 현재 모델은 최대 1024 토큰만 입력 가능합니다. 긴 논문은 앞부분 위주로 요약됩니다.
* SentencePiece 기반 모델 사용을 위해 `sentencepiece` 설치 필수입니다.
* 구조화된 요약 출력을 위해 강제 프롬프트를 삽입하고 있습니다. 완벽한 항목 출력은 보장되지 않습니다.

---

## ✨ 향후 개선 아이디어

* 사용자 정의 질문 입력 → QA 기반 요약으로 확장
* LoRA 기반 SFT로 구조화 성능 향상
* 논문 섹션 자동 추출 및 항목별 요약
* PDF 메타데이터 분석 포함

--- 