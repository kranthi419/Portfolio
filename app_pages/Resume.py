import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import base64

# The below implementation is not supported by the chrome.
# with open("./data/Kavali_Kranthi_Kumar_ML_Engineer.pdf", "rb") as f:
#     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64, {base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

with st.container(border=True):
    pdf_viewer("./data/Kavali_Kranthi_Kumar_ML_Engineer.pdf")
