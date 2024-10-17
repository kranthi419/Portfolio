import streamlit as st

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})


def clear_chat():
    st.session_state.messages = []


@st.cache_resource
def initialize_qa_chain():
    documents = SimpleDirectoryReader("./data/resume").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(streaming=True)
    return query_engine


def run(instruction):
    qa_agent = initialize_qa_chain()
    generated_text = qa_agent.query(instruction)
    return generated_text
