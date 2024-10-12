import streamlit as st

from utils.helpers import resize_image
from constants import info_about_me


st.subheader('🙋‍♂️ About me:')
st.write(info_about_me)


st.subheader('🔧 My Skills:')
st.write("""
[![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org)  [![](https://img.shields.io/badge/Machine-Learning-000?style=for-the-badge)](https://en.wikipedia.org/wiki/Machine_learning)
[![](https://img.shields.io/badge/DL-Deep%20Learning-blue?style=for-the-badge)](https://en.wikipedia.org/wiki/Deep_learning)
[![](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-yellow?style=for-the-badge)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![](https://img.shields.io/badge/CV-Computer%20Vision-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Computer_Vision)
[![](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)](https://mlflow.org)
[![](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)]()
[![](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)]()
[![](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)]()
[![](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)]()
[![](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)]()
[![](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org)
[![](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![](https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white)](https://www.scipy.org) 
[![](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org) 
[![](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org) 
[![](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com) 
[![](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org)
[<img src = "https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>](https://www.mongodb.com/)
[![](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/json-en.html) 
[![](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white)](https://keras.io)
[![](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com) 
[<img src = "https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" width = "100" height = "27.5"/>](https://www.sqlite.org/index.html)
[![](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/en-us/microsoft-365/excel) 
[![](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)](https://www.microsoft.com/en-us/microsoft-365/powerpoint) 
[![](https://img.shields.io/badge/Microsoft_Office-D83B01?style=for-the-badge&logo=microsoft-office&logoColor=white)](https://www.office.com)
[![](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://en.wikipedia.org/wiki/Git)

**Still Many More.....**""", unsafe_allow_html=True)


st.subheader('👨‍🎓 Certifications:')
with st.container():
    col = st.columns(3, gap="small")
    col[2].image(resize_image(f"C:/Personal-LLM-Projects/Portfolio-Website/data/DL specilization.jpg", 200),
                 caption="Deep Learning Specialization")
    col[1].image(resize_image(f"C:/Personal-LLM-Projects/Portfolio-Website/data/Oracle Cloud Infrastructure 2024 Generative AI Certified Professional.png", 250),
                 caption="Oracle Cloud Infrastructure 2024 Generative AI Certified Professional")
    col[0].image(resize_image(f"C:/Personal-LLM-Projects/Portfolio-Website/data/ML specialition.jpeg", 250),
                 caption="Machine Learning Specialization")

st.subheader('📝Research Papers:')
st.markdown("[<h5><u>Iris recognition based on Gabor and Deep Convolutional Networks</h5>](https://ieeexplore.ieee.org/document/9484905)", unsafe_allow_html=True)
st.markdown("[<h5><u>Effective Deep Learning approach based on VGG-Mini Architecture for Iris Recognition</h5>](http://annalsofrscb.ro/index.php/journal/article/view/5760)", unsafe_allow_html=True)
