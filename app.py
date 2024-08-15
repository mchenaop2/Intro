import streamlit as st
from PIL import Image

st.title ("Hello")

st.header("Peopleeee")
st.write("Amo viajar")
image = Image.open("Playa.jpeg")

st.image(image, caption="Beach")

texto = st.text_input("Gatossss" , "BRISA")
st.write("quesueñooo", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Primera columna")
  st.write("las interfaces multimodales")
  resp = st.checkbox("KHE")
  if resp:
    st.write("Nose")

with col2:
  st.subheader("segunda columna")
  modo = st.radio("ne se que estoy haciendo", ("Cami","brisa", "ehh"))
