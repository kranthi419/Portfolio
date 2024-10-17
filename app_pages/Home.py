import streamlit as st
import streamlit.components.v1 as components

from utils.helpers import resize_image
from constants import info_about_me


st.markdown("<h2 style='margin-bottom:0'>🙋‍♂️ About me:</h2>", unsafe_allow_html=True)
info_cols = st.columns([2, 1])
with info_cols[0]:
    st.markdown("### Kavali Kranthi Kumar")
    st.markdown("##### 📌Hyderabad, India")
    st.write(info_about_me)
with info_cols[1]:
    components.iframe("https://lottie.host/embed/4db26c4d-f195-4d1a-b0f0-ca43f2da848f/OOC3aEi0X4.json", height=400)

st.markdown("<h2 style='margin-bottom:0'>👨‍💻 Experience:</h2>", unsafe_allow_html=True)
st.markdown("### Senior Machine Learning Engineer at [**Synopsys Inc**](https://www.synopsys.com/)")
st.markdown("##### 📆 2024, June - Present")
st.markdown("Innomatics Research Labs is a pioneer in the field of Data Science and AI. I work as a Machine Learning Engineer and my responsibilities include developing and deploying machine learning models, training and mentoring interns, and working on real-time projects.")
st.markdown("### Machine Learning Engineer 2 at [**Phenom**](https://www.phenom.com/)")
st.markdown("##### 📆 2021, June - 2024, June")
st.markdown("I worked as a Data Science Intern at Innomatics Research Labs. I have worked on various projects and gained experience in Machine Learning, Deep Learning, and Natural Language Processing.")

st.markdown('#')
st.markdown("<h2 style='margin-bottom:0'>🔧 Skills:</h2>", unsafe_allow_html=True)
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

st.markdown('#')
st.markdown("<h2 style='margin-bottom:0'>👨‍🎓 Certifications:</h2>", unsafe_allow_html=True)
with st.container():
    col = st.columns(3, gap="small")
    col[2].image(resize_image(f"./data/DL specilization.jpg", 200),
                 caption="Deep Learning Specialization")
    col[1].image(resize_image(f"./data/Oracle Cloud Infrastructure 2024 Generative AI Certified Professional.png", 250),
                 caption="Oracle Cloud Infrastructure 2024 Generative AI Certified Professional")
    col[0].image(resize_image(f"./data/ML specialition.jpeg", 250),
                 caption="Machine Learning Specialization")
st.markdown('#')
st.markdown("<h2 style='margin-bottom:0'>📝 Research Works And Publications:</h2>", unsafe_allow_html=True)
st.markdown("[<h5><u>Iris recognition based on Gabor and Deep Convolutional Networks</h5>](https://ieeexplore.ieee.org/document/9484905)", unsafe_allow_html=True)
st.markdown("Nowadays, authorizing a person has become a significant need. Authorizing a person based on their behavioral or characteristic traits such as fingerprint, iris, face, etc. has brought in a lot of secure feelings in society. In our work, we present Iris-based Biometric systems that have been considered the most secure and accurate form of identifying an individual because of their unique features and textual richness present in them. In our work, we proposed two modified feature extraction techniques namely Convolutional Neural Networks (CNN) and Gabor filter, and then performed different classification algorithms namely SVM (Support Vector Machine) and Neural Networks (NN), and analyzed the change in accuracies affected by the features extracted from the two different techniques and finally landed with the best combination of CNN-NN with the accuracy of 98%. The CASIA Version 1 benchmark database has been used to perform our experiments for both testing and comparison.")
st.markdown("[<h5><u>Effective Deep Learning approach based on VGG-Mini Architecture for Iris Recognition</h5>](http://annalsofrscb.ro/index.php/journal/article/view/5760)", unsafe_allow_html=True)
st.markdown("Biometric system is a pattern recognition system that works by collecting biometric data from a user, extracting a feature set from that data, and comparing that feature set to a database template set. Through this paper, we propose a biometric recognition system based on iris recognition. Iris is the most secured and unique biometric trait among other biometric traits. In our work, we have proposed a modified Hough Transform and considered the Mini-VGG Net model without its weights, and trained the network to obtain the best features. Using the Neural Networks, we have performed the classification and obtained Accuracy, Precision, and Recall of 98%, 0.99, and 0.99 respectively. Our experiments were performed on the CASIA Version-1, which includes 756 samples of iris in 108 folders with 7 samples having dimensions 280X320 each.")
