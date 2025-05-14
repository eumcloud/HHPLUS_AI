 
---

## 커리어 업스킬링 프로젝트 

---

### 프로젝트 개요

> 현재 직무에서의 성장 또는 이직을 대비해, 시장에서 요구되는 스킬셋과 내 이력서를 비교하고, 부족한 역량을 보완하기 위한 커리큘럼을 자동 제안/관리하는 프로젝트입니다.

---

### 핵심 흐름 및 기능 요약

| 단계 | 설명 |
|------|------|
| 1. 커리어 JD 수집 | 네카라쿠베당토 + MS, Amazon, LinkedIn 등 주요 채용 플랫폼에서 관심 직무 관련 JD를 주기적으로 수집 |
| 2. 이력서 분석 | 내 기존 이력서를 기준으로 JD의 스킬셋과 비교 분석 |
| 3. 역량 비교 및 갭 분석 | JD에 있고 이력서에 없는 스킬, 있긴 하지만 부족한 스킬을 구분하여 분석 |
| 4. 커리큘럼 제시 | 갭을 채우기 위한 학습 경로 및 포트폴리오 미션을 자동 제안 |
| 5. 목표 트래킹 | 일정 기반 목표 관리 및 알림 기능 (예정) |

---

### 기술 스택

| 구성 요소 | 기술 |
|----------|------|
| 이력서 파서 | spaCy, PDFMiner, docx2txt |
| JD 크롤러 | Selenium, BeautifulSoup, REST API |
| 스킬 매칭 엔진 | embedding 기반 cosine similarity (Sentence-BERT) |
| 커리큘럼 추천 | LangChain + OpenAI API (기초 커리큘럼 GPT 생성) |
| 목표 트래커 | SQLite + Streamlit UI (예정) |

---

### 디렉토리 구조

```

career\_updater/
├── resume\_parser/
│   └── extract\_resume\_skills.py      # 이력서 내 기술 추출
├── jd\_collector/
│   ├── crawl\_job\_descriptions.py     # JD 수집 모듈
│   └── parse\_jd\_skills.py            # JD 내 기술 추출
├── skill\_matcher/
│   └── compare\_skills.py             # JD와 이력서 간 스킬 매칭 및 유사도 분석
├── curriculum\_recommender/
│   └── generate\_curriculum.py        # 부족한 스킬에 대한 커리큘럼 생성
├── portfolio\_suggester/
│   └── project\_ideas.py              # 포트폴리오 제안 기능
├── ui/
│   └── streamlit\_app.py              # Streamlit 대시보드 (개발 예정)
├── data/
│   ├── my\_resume.pdf
│   └── jd\_snapshots/
├── requirements.txt
└── README.md

```

---

### 주요 기능 예시

| 입력 예시 | 출력 결과 |
|----------|-----------|
| `내 이력서.pdf` + `JD 10건` | JD 대비 부족한 스킬 목록 + 학습 커리큘럼 + 프로젝트 제안 |
| JD: `ML Ops 엔지니어` | 필요 스킬: Airflow, Docker, KFP → 학습 루트 제안 |
| JD: `LLM 파이프라인 엔지니어` | 필요 스킬: LangChain, Vector DB → 학습 + RAG 포트폴리오 |

---

### 목표 항목

| 항목 | 구현 파일/모듈 | 설명 |
|------|----------------|------|
| JD 수집 자동화 | `jd_collector/crawl_job_descriptions.py` | 크론 기반 정기 실행 예정 |
| 이력서 기반 스킬 파서 | `resume_parser/extract_resume_skills.py` | pdf/docx에서 기술 추출 |
| 스킬 매칭 및 커리큘럼 추천 | `skill_matcher/` + `curriculum_recommender/` | 갭 분석 후 GPT 기반 커리큘럼 생성 |
| 포트폴리오 제안 | `portfolio_suggester/project_ideas.py` | JD 기반 미니 프로젝트 아이디어 |
| 대시보드 제공 | `ui/streamlit_app.py` | 알림/현황 트래커 기능 포함 (개발 예정) |

--- 