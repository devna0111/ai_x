# ctrl+ shift + p : interpretter 선택
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="첫번째 프로그램")

st.title("나의 첫 Streamlit 앱")
st.subheader("웹 앱을 만들기 위한 강력한 라이브러리 : Streamlit")

st.info('text 출력')
message = st.text_area('여기에 줄글을 입력하세요')
if message :
    st.info('Hello, Streamlit')


