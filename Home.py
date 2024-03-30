import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

chat=None #openai实例对象

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] =""
else:
    chat=ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"]=""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state['PINECONE_ENVIRONMENT']=""

st.set_page_config(page_title="Welcome to ASL",layout="wide")

st.title("Welcome to ASL")

if chat:
    with st.container():
        st.header("Chat with GPT")
        prompt=st.text_input("Prompt",value="",max_chars=None,key=None,type='default') #保存用户输入
        asked=st.button("Ask")
        if asked:
            ai_message=chat([HumanMessage(content=prompt)]) #ai内容
            st.write(ai_message.content)
else:
    with st.container():
        st.warning("Please set your api key")

