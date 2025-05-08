# 🧠 멀티모달 패션 챗봇 

이 노트북은 Streamlit과 OpenAI Vision 모델을 이용하여 멀티모달 챗봇을 구현하는 과정을 단계별로 정리합니다

---

## 🪜 목표 목록

- [x] 단일 이미지 입력 및 응답 (기존 코드)
- [ ] 여러 이미지 입력 받기
- [ ] 사용자 입력 기반 자유 질의응답
- [ ] 이미지 정보 유지하며 반복 질문 가능하게 하기 (메모리)
- [ ] 실제 챗봇 사용 테스트 (강아지+고양이 사진, 2가지 질문)

---


1. 준비


```python
# 필요한 라이브러리 설치
%pip install --quiet streamlit langchain langchain-openai openai python-dotenv
```

    Note: you may need to restart the kernel to use updated packages.



```python
import base64
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

```

2. API KEY 설정


```python
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY") 
model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

```

3. 단일 이미지 + 고정 프롬프트 챗봇 구현


```python
st.title("Fashion Recommendation Bot")
model = ChatOpenAI(model="gpt-4o-mini")
if image := st.file_uploader("본인의 전신이 보이는 사진을 올려주세요!", type=['png', 'jpg', 'jpeg']):
    st.image(image)
    image = base64.b64encode(image.read()).decode("utf-8")
    with st.chat_message("assistant"):
        message = HumanMessage(
            content=[
                {"type": "text", "text": "사람의 전신이 찍혀있는 사진이 한 장 주어집니다. 이 때, 사진 속 사람과 어울리는 옷 및 패션 스타일을 추천해주세요."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image}"},
                },
            ],
        )
        result = model.invoke([message])
        response = result.content
        st.markdown(response)
```

4. 다중 이미지 업로드 기능 추가


```python
images = st.file_uploader("이미지를 여러 장 업로드하세요", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
image_b64_list = []

if images:
    for image in images:
        st.image(image)
        b64 = base64.b64encode(image.read()).decode("utf-8")
        image_b64_list.append(
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
        )

```

5. 사용자 자유 질문 + 반복 대화 구현


```python
if "messages" not in st.session_state:
    st.session_state.messages = image_b64_list.copy()

query = st.chat_input("질문을 입력하세요")

if query:
    st.chat_message("user").write(query)
    message = HumanMessage(
        content=[
            {"type": "text", "text": query},
            *st.session_state.messages
        ]
    )
    response = model.invoke([message])
    st.chat_message("assistant").write(response.content)

```

✅ 마무리 체크리스트
 .env를 통해 API 키 안전하게 설정

 다중 이미지 업로드 기능 구현

 유저 입력 기반 질의응답 챗봇 구현

 이미지 기억을 활용한 반복 대화 구현

 강아지/고양이 예시로 챗봇 테스트 완료 
