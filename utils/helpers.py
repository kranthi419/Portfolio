import time
import streamlit as st
from PIL import Image


def stream_data(data):
    for text in data.split(" "):
        yield text + " "
        time.sleep(0.05)


def initialize_variable(name, default=None):
    if name not in st.session_state:
        st.session_state[name] = default



def resize_image(image_path, target_height):
    img = Image.open(image_path)
    width, height = img.size
    new_width = int(target_height * width / height)
    resized_img = img.resize((new_width, target_height))
    return resized_img
