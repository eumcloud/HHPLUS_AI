 # 📄 논문 요약 LLM 서비스

**경량 LLM 기반 논문 요약 웹 애플리케이션**입니다.
사용자는 PDF 파일 업로드 또는 링크 입력을 통해 논문을 제공하고, Hugging Face Inference API를 통해 구조화된 요약을 받을 수 있습니다.

## 서비스 개요

* 사용자는 Streamlit UI에서 논문 PDF를 **업로드**하거나, **PDF 링크를 입력**할 수 있습니다.
* 논문 텍스트는 전처리 후, \*\*LLM(LLaMA 3 8B Instruct)\*\*에 입력됩니다.
* LLM은 다음과 같은 형식으로 논문을 요약합니다:

```
1. 제목 요약:
2. 연구 목적:
3. 방법론 요약:
4. 주요 실험 결과:
5. 기여 및 의의:
6. 응용 가능성:
```

---

## 사용한 기술 스택

| 구성 요소           | 설명                                                               |
| --------------- | ---------------------------------------------------------------- |
| **Frontend**    | Streamlit                                                        |
| **LLM Backend** | Hugging Face Inference API (meta-llama/Meta-Llama-3-8B-Instruct) |
| **문서 처리**       | PyMuPDF (fitz)                                                   |
| **환경 관리**       | dotenv (.env)                                                    |

---

## 시연 조건 

* [x] **PDF 업로드** 기능
* [x] **PDF 링크 입력** 기능
* [x] **질문 입력 후 요약 출력** 
* [x] **Streamlit UI로 유연한 입력 지원**
* [x] **지연 실행 구조로 페이지 빠르게 로딩됨**

---

## 시연준비

### 1. 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일 생성:

```bash
HF_TOKEN=hf_your_huggingface_token
```

> 권한은 **Inference API (Read-only)** 만 필요

### 3. 실행

```bash
streamlit run app.py
```

---

## 📂 프로젝트 구조

```
.
├── app.py               # Streamlit 메인 앱
├── README.md
├── requirements.txt
├── .env.example         # 환경 변수 템플릿
└── .gitignore
```

---

## 입력 예시 (Instruction 3종)

### ① 논문 목적과 기여 요약

> "이 논문의 핵심 목적과 주요 기여를 요약해줘"

### ② 방법론 위주로 분석

> "사용된 방법론과 모델 아키텍처만 중심으로 설명해줘"

### ③ 응용 가능성과 한계

> "이 연구의 실용적 활용 가능성과 한계를 평가해줘"

---

## 배포

* AWS EC2 + Streamlit + Nginx로 배포 가능
* 또는 Hugging Face Spaces로도 경량화된 버전 배포 가능

---

## 기타 확장 아이디어

* RAG + 벡터 검색 구조로 고도화
* LangChain 기반 문서 QA 서비스로 확장
* 사용자 질문 히스토리 + 요약 결과 저장 기능 추가

--- 