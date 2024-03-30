import streamlit as st

#st.session_state是一个字典，可以用来保存和跟踪用户的状态和信息
if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"]=""

#设置环境
if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"]=""

st.title("Pinecone Settings")

pinecone_api_key = st.text_input("API Key", value=st.session_state["PINECONE_API_KEY"],max_chars=100,key=None,type='default')
environment_api_key = st.text_input("ENVIRONMENT", value=st.session_state["PINECONE_ENVIRONMENT"],max_chars=100,key=None,type='default')

saved=st.button("Save")

if saved:
    st.session_state["PINECONE_API_KEY"]=pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"]=environment_api_key


#显示Pinecone信息
with st.container():
    st.header("Pinecone Settings")
    st.markdown(f"""
       | OpenAI API KEY | Environment |
       | -------------- | ----------- |
       | {st.session_state["PINECONE_API_KEY"]} | {st.session_state["PINECONE_ENVIRONMENT"] } |
       """)
