import streamlit as st
from PIL import Image

st.title ("Hello")

st.header("Peopleeee")
st.write("Amo viajar")
image = Image.open("Playa.JPG")

st.image(image, caption="Beach")
