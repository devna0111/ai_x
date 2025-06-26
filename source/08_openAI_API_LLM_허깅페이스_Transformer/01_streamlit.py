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
# def askGPT(prompt) :
#     '''GPT에게 prompt 요청 결과 반환'''
#     client = OpenAI()
#     response = client.chat.completions.create(
#                 model = 'gpt-4.1-nano',
#                 messages = [
#                     {'role':'system','content':'당신은 한국어로 된 텍스트를 잘 요약하는 전문 어시스턴트입니다.'},
#                     {'role':'user', 'content':prompt},]
#                 )
#     return response.choices[0].message.content

# message = input("요약할 글을 입력하세요 : ")
# if message :
#     prompt = f""" 다음 텍스트를 세줄로 요약합니다. 글머리 기호 형식을 사용하세요.
#     텍스트 : {message}"""
#     result = askGPT(prompt)
#     print(result)