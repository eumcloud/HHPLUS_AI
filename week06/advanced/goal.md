
---

## ✅ 논문 요약 및 시각화 LLM 서비스 – README.md

---

### 📌 **서비스 컨셉**

> 논문(PDF 업로드 or arXiv 검색)을 입력 받아, 텍스트/표/그래프/이미지를 LLM이 요약 및 시각화한 리포트를 생성하는 Streamlit 기반의 웹 서비스입니다.

---

### 🛠️ **기술 스택 및 구성요소**

| 파트            | 기술                                                                       |
| ------------- | ------------------------------------------------------------------------ |
| 프론트엔드         | Streamlit                                                                |
| 백엔드           | Python, LangChain, OpenAI API                                            |
| 데이터 추출        | PyMuPDF, pdfplumber, OCR(Tesseract), Table extractor(Camelot, Tabula-py) |
| 이미지 처리        | matplotlib, PIL, OpenCV                                                  |
| 서빙            | BentoML, FastAPI *(선택)*                                                  |
| 배포            | ~~AWS EC2~~, Streamlit Cloud                                                 |
| 파이프라인 관리      | Airflow, Kubeflow Pipelines                                              |
| 실험 추적 및 MLOps | MLflow, tqdm, 로그 및 성능 지표 관리                                              |

---

### 🎯 주요 기능

#### 1. 논문 입력

* PDF 업로드 또는 키워드 기반 논문 검색(arXiv API)

#### 2. 논문 텍스트 요약

* LangChain + OpenAI (GPT-4 기반) 전체 요약 및 섹션별 요약 지원

#### 3. 이미지 / 표 / 그래프 추출 및 해석

* 논문 내 이미지, 표 등 시각자료를 인식하고 시각화로 재구성

#### 4. 시각적 보고서 생성 및 다운로드

```
/root
│
├── app.py                           # Streamlit 실행 진입점
│
├── llm_modules/                     # LLM 기반 기능 모듈
│   ├── paper_summarizer.py         # 논문 텍스트 요약 기능 (LangChain, OpenAI API)
│   ├── visual_extractor.py         # 이미지/표/그래프 추출 및 처리
│   ├── report_generator.py         # 시각화 포함 종합 리포트 생성
│   └── paper_search.py             # 논문 API 검색 (e.g., arXiv, Semantic Scholar)
│
├── pipelines/                      # 데이터 처리 파이프라인 (MLOps 관점)
│   └── summary_pipeline.py         # 입력 → 요약 → 시각화 일련의 처리 흐름
│
├── ui_components/                  # Streamlit UI 구성요소 분리
│   ├── upload_pdf.py               # PDF 업로드 및 처리
│   ├── search_interface.py         # 논문 검색 UI
│   └── visualization.py            # 그래프, 표 시각화 UI
│
├── assets/                         # 테스트용 PDF, 이미지, 표, 샘플 데이터
│   ├── sample_paper.pdf
│   ├── example_table.png
│   └── demo_chart.jpg
│
├──ops/
│  ├── Dockerfile
│  ├── docker-compose.dev.yml
│  ├── terraform/
│  │    ├── main.tf   # S3 + ECR + EC2
│  └── airflow_dag/
│       └── paper_summary_daily.py
│
├── demo_video.mp4                  # 3가지 기능 데모 영상
├── requirements.txt                # 필수 라이브러리 목록
├── README.md                       # 서비스 설명, 사용법, 기능 정리
└── .streamlit/
    └── config.toml                 # Streamlit 앱 설정
```

---

#### 5. 실험 기록 및 분석

* MLflow를 통해 요약 결과, 처리 시간, 토큰 수 등을 기록하고 비교 가능

---

### 📊 Streamlit UI Flow

```mermaid
graph TD
    Start["시작 화면 (Streamlit)"] --> InputSelect["입력 방식 선택"]
    InputSelect --> Upload["PDF 업로드 (upload_pdf.py)"]
    InputSelect --> Search["논문 검색 (search_interface.py)"]
    Upload --> ExtractText["텍스트 추출 (visual_extractor.py)"]
    Search --> ExtractText

    ExtractText --> Summarize["논문 요약 (paper_summarizer.py)"]
    Summarize --> ExtractVisuals["이미지/표 추출 (visual_extractor.py)"]
    ExtractVisuals --> GenerateReport["리포트 생성 (report_generator.py)"]

    GenerateReport --> MLflow["MLflow 실험 기록 (mlflow_tracking.py)"]
    GenerateReport --> Visualize["시각화 출력 (visualization.py)"]
    Visualize --> Download["리포트 다운로드 버튼 (app.py)"]

```

---

### 💡 UI 구성 요약

| UI 영역 | 구성 모듈                                                  |
| ----- | ------------------------------------------------------ |
| 사이드바  | 논문 입력 선택 (PDF vs 검색)                                   |
| 본문 상단 | 요약 결과 텍스트 표시 (`paper_summarizer.py`)                   |
| 본문 중간 | 이미지, 표 시각화 (`visual_extractor.py`, `visualization.py`) |
| 본문 하단 | 리포트 다운로드 버튼 (`app.py`)                                 |

---

### 🧪 시나리오 예시 (Instruction 3종)

| 입력                          | 출력 결과                         |
| --------------------------- | ----------------------------- |
| PDF 논문 업로드                  | 전체 요약 + 표 시각화 + 이미지 해석 포함 리포트 |
| arXiv 키워드 검색                | 논문 검색 결과 → 선택 → 요약 리포트 출력     |
| 특정 섹션 요약 요청 (e.g. methods만) | 해당 섹션만 추출 및 요약 결과 출력          |

---

### 📁 프로젝트 구조

```
.
├── app.py                       # Streamlit 앱
├── llm_modules/                 # LLM 기반 논문 분석 모듈
│   ├── paper_summarizer.py
│   ├── visual_extractor.py
│   ├── report_generator.py
│   └── paper_search.py
├── ui_components/              # Streamlit 입력/출력 UI 모듈
│   ├── upload_pdf.py
│   ├── search_interface.py
│   └── visualization.py
├── pipelines/                  # 파이프라인 처리 흐름 (Airflow 등)
│   ├── summary_pipeline.py
│   ├── airflow_dag.py
├── monitoring/                 # MLflow 기반 실험 추적
│   └── mlflow_tracking.py
├── serving/                    # BentoML 기반 모델 서빙
│   └── bento_service.py
├── rag_modules/                # 검색 기반 요약 시스템 (RAG)
│   ├── index_builder.py
│   ├── rag_pipeline.py
│   └── retriever.py
├── kfp/                        # Kubeflow Pipeline 관련 구성
│   ├── components/
│   │   ├── extract_text.py
│   │   └── summarize.py
│   ├── interface_service.yaml
│   └── kfp_pipeline.py
├── assets/                     # 샘플 데이터
│   ├── sample_paper.pdf
│   └── example_table.png
├── requirements.txt
└── README.md
```

---

### 🧩 목표

| 항목               | 구현 모듈/경로                         | 설명                                |
| ------------------- | -------------------------------- | --------------------------------- |
| ML 파이프라인          | `/pipelines/`, `/kfp/`           | Airflow DAG, Kubeflow Pipeline 구성 |
| LLM 서빙 시스템          | `/serving/bento_service.py`      | BentoML로 REST API 서빙              |
| 성능 모니터링 및 실험 관리     | `/monitoring/mlflow_tracking.py` | MLflow + 로그 기록                    |
| RAG 기반 검색 요약        | `/rag_modules/`                  | 벡터 DB 기반 검색 + 요약                  |
| Kubeflow 기반 클러스터 운영 | `/kfp/kfp_pipeline.py` + YAML    | 전체 요약 파이프라인 KFP로 실행               |


--- 
