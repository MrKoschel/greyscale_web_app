import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

uploaded_file = st.file_uploader("Upload image")
if uploaded_file:
    img = Image.open(uploaded_file)
    uploaded_file_grey = img.convert("L")
    st.image(uploaded_file_grey)
