import streamlit as st
import base64

# we can also use -> https://github.com/lfoppiano/streamlit-pdf-viewer
with open("./data/Kavali_Kranthi_Kumar_ML_Engineer.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64, {base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
