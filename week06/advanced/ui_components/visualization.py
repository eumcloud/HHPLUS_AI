import streamlit as st
from PIL import Image

def show_visualizations(images: list):
    if images:
        st.subheader("📷 추출된 시각 자료")
        for idx, img in enumerate(images):
            st.image(img, caption=f"추출 이미지 {idx+1}", use_column_width=True)
    else:
        st.info("추출된 이미지가 없습니다.")
