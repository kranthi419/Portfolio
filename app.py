import streamlit as st
import streamlit.components.v1 as components

from chatbot.qa_agent import add_message, display_chat_history, clear_chat, run
from utils.helpers import stream_data, initialize_variable
from constants import intro_message, linkedin_url

st.set_page_config(
    page_title="kavali-kranthi-kumar-portfolio",
    layout="wide",
    page_icon="🧑‍💻")

initialize_variable(name="shown_intro_message", default=True)


@st.dialog("Hello, I'm Kavali Kranthi Kumar🧑‍💻")
def start():
    st.write_stream(stream_data(intro_message))


if st.session_state.shown_intro_message:
    start()
    st.session_state.shown_intro_message = False

with st.sidebar:
    components.html(linkedin_url, height=320)
    st.caption('Wish to connect?')
    st.write('📧: kavalikranthikumar3@gmail.com')
    st.write('📞: +91-9505530176')

resume_page = st.Page(page="app_pages/Resume.py", title="View Resume:")
home_page = st.Page(page="app_pages/Home.py", title="Home:")
projects_page = st.Page(page="app_pages/Projects.py", title="Expertise:")
pg = st.navigation({"Application:": [home_page, projects_page, resume_page]})
pg.run()


initialize_variable(name="messages", default=[])
initialize_variable(name="api_key", default=None)
# Custom CSS for larger popover and other styling
st.markdown("""
<style>
.stPopover {
    position: fixed;
    bottom: 20px;
    right: 20px;
}
.stChatMessage { margin-bottom: 10px; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stChatFloatingInputContainer {
    bottom: 60px;
}
.main > div:last-child {
    padding-bottom: 120px;
}
/* Larger popover styles */
.stPopover > div[data-modal-container="true"] > div[data-modal-content="true"] {
    width: 80vw !important;
    max-width: 800px !important;
    height: 80vh !important;
    max-height: 800px !important;
}
.stPopover > div[data-modal-container="true"] > div[data-modal-content="true"] > div:first-child {
    height: calc(100% - 60px) !important;
    overflow-y: auto;
}
.clear-button {
    position: absolute;
    top: 5px;
    right: 5px;
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)
chat_popup_col, _ = st.columns([2, 2])
with chat_popup_col.popover("🤖ResumeGPT📄", use_container_width=True):
    if st.session_state.api_key is None:
        st.write("Please enter your OpenAI API key to start chatting.")
        st.text_input("**OpenAI API Key:**", type="password", key="api_key")
    if not st.session_state.api_key.startswith("sk-"):
        st.warning("Please enter valid OpenAI API key to start chatting.")
        st.text_input("**OpenAI API Key:**", type="password", key="api_key")
    # Clear Chat button
    clear_col, api_api_input = st.columns([1, 3])
    with clear_col:
        if st.button("Clear Chat💬", key="clear_chat", help="Clear the chat history"):
            clear_chat()
            st.rerun()

    chat_container = st.container()
    with chat_container:
        display_chat_history()

    # Chat input within the popover
    prompt = st.chat_input("What's on your mind?")

    if prompt:
        st.chat_message("user").markdown(prompt)
        add_message("user", prompt)
        with st.chat_message("assistant"):
            with st.spinner():
                response = run(prompt)
                st.markdown(response)
        add_message("assistant", response)

        # Force a rerun to update the chat history immediately
        st.rerun()
