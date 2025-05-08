

---

### ✅ **서비스 컨셉: 논문 요약 및 시각화 LLM 서비스**

> 논문(PDF or API 검색 기반)을 입력받아 텍스트/이미지/표/그래프를 인식하고, 이를 LLM이 요약 및 재구성한 후, 시각적으로 리포트를 생성해주는 streamlit 기반 웹 서비스

---

### 🛠️ **기술 스택 및 구성요소**

| 파트         | 기술                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------- |
| 프론트엔드      | Streamlit                                                                                         |
| 백엔드        | Python, LangChain, OpenAI API                                                                     |
| 데이터 추출     | PDF parser (PyMuPDF, pdfplumber), OCR (Tesseract or PaddleOCR), Table extractor (Camelot, Tabula) |
| 이미지 처리     | matplotlib, PIL, OpenCV                                                                           |
| 배포         | AWS EC2 / Streamlit Cloud                                                                         |
| 로그 및 실험 추적 | MLflow (optional, MLOps 관점)                                                                       |
| 파이프라인 관리   | Airflow or 간단한 task orchestrator로 확장 고려                                                           |

---

### 🎯 기능 요구사항과 구현 아이디어

#### 1. **PDF 업로드 및 요약**

* 사용자는 논문 PDF를 업로드하거나 API 검색으로 논문을 선택
* LangChain + OpenAI로 요약 생성
* 요약 종류: 전체 요약 / 섹션별 요약 / 키포인트 요약

#### 2. **이미지, 표, 그래프 인식 및 재구성**

* PDF에서 이미지/표 추출

  * 이미지: OCR로 설명 추출
  * 표: Camelot으로 CSV화, df → 그래프 변환
* 추출 내용을 기반으로 요약 문단 내 시각 자료 생성

  * 예: matplotlib로 표 시각화, OCR 설명으로 캡션 생성

#### 3. **시각적 보고서 생성**

* Streamlit에서 markdown, image, chart 요소를 조합해 보고서 형태로 표시
* 다운로드 가능 (PDF or HTML)

#### 4. **API 검색 기능 (선택 기능)**

* Semantic Scholar, arXiv API 활용해 논문 검색 → 다운로드 → 요약 진행

---

### 📦 MLOps 관점 포인트

| 항목             | 설명                                             |
| -------------- | ---------------------------------------------- |
| **데이터 처리 자동화** | 텍스트, 표, 이미지 각각 파이프라인 분리                        |
| **실험 추적**      | 요약 결과 비교 (길이, 정확도), LLM 모델 변경 시 성능 추적 (MLflow) |
| **에러 핸들링**     | PDF 파싱 실패, OCR 실패 등 예외 처리 로깅                   |
| **서비스화**       | Streamlit + AWS 배포로 실제 사용 가능한 웹 서비스 구현         |
| **유지보수성**      | LangChain Chain 관리, config-based 구조 설계         |
| **CI/CD (확장)** | Github Actions 통해 테스트 및 배포 자동화 가능              |

---

### 🧪 제출 예시 시나리오 (3가지 instruction)

| 입력                           | 결과                      |
| ---------------------------- | ----------------------- |
| PDF 논문 업로드                   | 전체 요약 + 표 시각화 + 그래프 재구성 |
| 논문 제목으로 검색                   | arXiv에서 검색 → 요약 결과 출력   |
| 특정 섹션 요약 요청 (e.g. "methods") | 해당 부분만 정리된 요약 생성        |

---
좋습니다! 당신의 서비스 목적(논문 요약 + 이미지/표/그래프 분석 및 시각화)에 맞춘 GitHub 제출자료 구성 예시는 아래와 같이 구상할 수 있습니다.

---

## 📁 구성 (GitHub 기준)

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
├── demo_video.mp4                  # 3가지 기능 데모 영상
├── requirements.txt                # 필수 라이브러리 목록
├── README.md                       # 서비스 설명, 사용법, 기능 정리
└── .streamlit/
    └── config.toml                 # Streamlit 앱 설정
```

---

### ✅ 보완 포인트

* **modular structure**로 유지보수 용이
* 기능별 디렉토리 분리 (LLM, 파이프라인, UI 등)
* `pipelines/` 폴더에 MLOps 파이프라인을 추가하면 향후 확장 가능
* `assets/`에는 실습 영상에서 사용할 샘플 데이터를 충분히 포함
 

---

### 📊 Streamlit UI Flow  
---
 

```mermaid
graph TD
    A[시작 화면 (Streamlit)] --> B{입력 방식 선택}
    B --> C[PDF 업로드 (ui_components/upload_pdf.py)]
    B --> D[논문 검색 (ui_components/search_interface.py)]

    C --> E[텍스트 추출 (llm_modules/visual_extractor.py)]
    D --> E

    E --> F[논문 요약 (llm_modules/paper_summarizer.py)]
    F --> G[이미지/표 추출 (llm_modules/visual_extractor.py)]
    G --> H[리포트 생성 (llm_modules/report_generator.py)]

    H --> I[MLflow 실험 기록 (monitoring/mlflow_tracking.py)]
    H --> J[시각화 출력 (ui_components/visualization.py)]

    J --> K[리포트 다운로드 버튼]
```

---

## 💡 각 단계별 실제 코드 매핑

| 단계          | 담당 모듈                   |
| ----------- | ----------------------- |
| 📂 입력 선택    | `app.py` 사이드바           |
| 📂 PDF 업로드  | `upload_pdf.py`         |
| 📂 논문 검색    | `search_interface.py`   |
| 📂 텍스트 추출   | `visual_extractor.py`   |
| 📂 요약 처리    | `paper_summarizer.py`   |
| 📂 이미지/표 추출 | `visual_extractor.py`   |
| 📂 리포트 구성   | `report_generator.py`   |
| 📂 실험 로깅    | `mlflow_tracking.py`    |
| 📂 시각화 출력   | `visualization.py`      |
| 📂 다운로드 기능  | `app.py` 내 Streamlit UI |

--- 

---

### 💡 주요 UI 구성 대응 예시

| UI 영역 | 내용                   |
| ----- | -------------------- |
| 사이드바  | 논문 입력 선택 (업로드 vs 검색) |
| 본문 상단 | 논문 요약 결과 (텍스트 기반)    |
| 본문 중간 | 표 및 이미지 자동 인식 및 시각화  |
| 본문 하단 | 전체 리포트 다운로드 버튼       |


---

## 추가 목표 

| JD 항목                   | 구현 대상                                  | 반영 위치 (폴더/파일)                | 설명                                                      |
| ----------------------- | -------------------------------------- | ---------------------------- | ------------------------------------------------------- |
| 🛠 머신러닝 파이프라인           | `Airflow` or `Kubeflow`                | `/pipelines/`                | `summary_pipeline.py`를 DAG 또는 KFP 형태로 확장                |
| 🚀 모델 서빙 시스템            | `BentoML`, `TorchServe`, `Triton`      | `/serving/` *(신규 폴더 추가)*     | `bento_service.py`에 LLM 요약 API 구현                       |
| 📊 성능 모니터링 / 실험관리       | `MLflow`, `tqdm`                       | `/monitoring/` *(신규 폴더 추가)*  | `mlflow_tracking.py`, 로그 및 평가 스크립트                      |
| 🧠 RAG / 벡터 검색 / 로컬 LLM | `LangChain Retriever`, `FAISS`, `LoRA` | `/rag_modules/` *(신규 폴더 추가)* | `rag_pipeline.py`, `index_builder.py`, `retriever.py` 등 |
| ⚙️ Kubeflow 기반 운영       | `kfp` pipeline 정의, YAML 서빙 spec        | `/kfp/` *(신규 폴더 추가)*         | `kfp_pipeline.py`, `inference_service.yaml` 등           |
| 💸 금융 특화 데이터처리          | PDF → 공시, 보고서 등 대체                     | `/assets/` + `/rag_modules/` | 금융 문서 샘플 추가 + domain chunk/rag 구성                       |


---
