---

## 멀티모달 패션 챗봇 (실습 과제)

이 프로젝트는 OpenAI GPT-4o 모델과 Streamlit을 활용하여 **이미지를 기반으로 자연어 질의응답이 가능한 패션 챗봇**을 구현하는 실습입니다.

초기 실습에서는 단일 이미지 + 고정된 프롬프트로 응답을 받았다면, 이번 확장 실습에서는 **다중 이미지 + 사용자 자유 질문 + 반복 대화 기능**을 포함한 멀티모달 챗봇을 완성하는 것이 목표입니다.

---

## 목표

| 목표                    | 설명                           |
| --------------------- | ---------------------------- |
| ✅ 단일 이미지 + 고정 질문 처리   | 기존 코드에서 구현됨                  |
| ✅ 여러 이미지 입력 처리        | `accept_multiple_files=True` |
| ✅ 사용자 자유 질문 처리        | `st.chat_input()` 활용         |
| ✅ 이미지 유지 + 반복 질의응답 가능 | `st.session_state` 활용        |
| ✅ 실사용 테스트 영상 촬영       | 고양이/강아지 이미지 + 질문 2개로 데모      |

---

## 💡 기능 설명

* **다중 이미지 업로드**
  여러 장의 이미지를 한 번에 업로드 가능하며, 모든 이미지를 GPT-4o에 함께 전달하여 응답을 생성합니다.

* **자유 질의응답 지원**
  사용자가 입력한 질문을 기반으로 답변을 생성하며, 매 질문마다 이전 업로드 이미지를 참고합니다.

* **이미지 기억 기능 (메모리)**
  한 번 업로드된 이미지는 세션 내내 기억되며, 반복 질의 시 계속 반영됩니다.

* **Streamlit UI 최적화**
  채팅 입력창은 항상 하단에 고정되고, 업로드 버튼은 그 바로 위에 배치됩니다.

---

## 🖥️ 실행 방법

```bash
# 1. 필요한 패키지 설치
pip install streamlit openai langchain langchain-openai python-dotenv

# 2. OpenAI API 키 설정 (.env)
OPENAI_API_KEY=sk-...

# 3. 앱 실행
streamlit run app.py
```

---

## 📁 디렉토리 구조

```
├── app.py           # Streamlit 앱 코드
├── .env             # OpenAI API 키 보관용
└── README.md        # 설명 문서
```

---

## 📷 실습 영상 가이드

다음 조건에 맞춰 챗봇과의 대화를 시연하고 GIF 또는 영상으로 녹화합니다:

* **이미지 업로드**: 고양이 1장 + 강아지 1장
* **질문 1**: 주어진 두 사진의 공통점이 뭐야?
* **질문 2**: 주어진 두 사진의 차이점이 뭐야?



---

## 🔗 참고 자료

* [OpenAI Vision API 문서](https://platform.openai.com/docs/guides/vision)
* [Streamlit file\_uploader](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader)
* [LangChain ChatOpenAI](https://js.langchain.com/docs/modules/model_io/chat/)

