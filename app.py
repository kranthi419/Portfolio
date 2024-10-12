import streamlit as st
import streamlit.components.v1 as components

from utils.helpers import stream_data, initialize_variable
from constants import intro_message, linkedin_url


st.set_page_config(
    page_title="kavali-kranthi-kumar-portfolio",
    layout="wide",
    page_icon="🧑‍💻",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
    )


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
