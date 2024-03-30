import streamlit as st
import openai

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] =""

#页面初始化
st.set_page_config(page_title="OpenAi Settings/test",layout="wide")

st.title("OpenAi Settings/test")
#输入key
openai.api_key=st.text_input("API key",value=st.session_state["OPENAI_API_KEY"],max_chars=200,key=None,type='password')

#保存用户输入
saved=st.button("Save")
if saved:
    st.session_state["OPENAI_API_KEY"]=openai.api_key


#显示OpenAI的相关信息
with st.container():
    st.header("OpenAI Settings")
    #表格显示API key
    openai_api_key = st.session_state['OPENAI_API_KEY']  # 先获取API密钥的值
    st.markdown(f"""
    | OpenAI API KEY |
    | -------------- |
    | {openai_api_key} |
    """)