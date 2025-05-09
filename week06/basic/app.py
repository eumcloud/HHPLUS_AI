import base64
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage  
from dotenv import load_dotenv
import os
import uuid


# 환경변수 로드 및 모델 설정
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

# 페이지 설정
st.set_page_config(page_title="패션 챗봇", layout="centered")  # 변경됨: 아이콘 제거
st.markdown("<style>.uploadedFile {display: none}</style>", unsafe_allow_html=True)  

if "initialized" not in st.session_state:
    st.session_state.messages = []
    st.session_state.image_messages = []
    st.session_state.uploaded_filenames = set()
    st.session_state.initialized = True  # 다시 열리면 초기화됨

if st.button("🔄 대화 초기화"):
    st.session_state.clear()
    st.session_state.reset_uploader = True

    st.success("대화가 초기화되었습니다. 다시 질문을 입력하세요.")
    



# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []  # HumanMessage, AIMessage 등을 담음
if "image_messages" not in st.session_state:
    st.session_state.image_messages = []  # base64 이미지 정보만 따로 저장


for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content[0]["text"])
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# 이미지 업로드 박스 배치
with st.container():
    uploaded_images = st.file_uploader(
        label="이미지를 업로드하세요",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        label_visibility="collapsed",
        # key="image_uploader" if "reset_uploader" not in st.session_state else str(uuid.uuid4())
        key="fixed_image_uploader"  # 고정 키 사용
    )
# 채팅 입력창은 항상 페이지 하단에 위치
query = st.chat_input("질문을 입력하세요")


# 이미지 업로드 시 base64 처리 후 image_messages에 저장
new_image_messages = []
if uploaded_images:
    for image in uploaded_images:
        st.image(image, width=200)
        b64 = base64.b64encode(image.read()).decode("utf-8")
        new_image_messages.append(
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
        )
    # st.session_state.image_messages.extend(new_image_messages)
    # 새로 업로드한 이미지만 유지 (세션 전역 누적 X)
    st.session_state.image_messages = new_image_messages


# 사용자 입력 처리
if query:
    st.chat_message("user").write(query)

    # 모든 질문에 이미지 포함
    user_msg = HumanMessage(
        content=[{"type": "text", "text": query}, *st.session_state.image_messages]
    )
    st.session_state.messages.append(user_msg)

    # 전체 대화 시퀀스를 모델에 전달
    response = model.invoke(st.session_state.messages)
    st.chat_message("assistant").write(response.content)

    # assistant 응답도 대화에 추가
    st.session_state.messages.append(AIMessage(content=response.content))
