import streamlit as st
from PIL import Image

st.title ("Hello")

st.header("Peopleeee")
st.write("Amo viajar")
image = Image.open("Playa.jpeg")

st.image(image, caption="Beach")

texto = st.text_input("Gatossss" , "BRISA")
st.write("quesueñooo", texto)
