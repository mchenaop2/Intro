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
    st.write("correcto")

with col2:
  st.subheader("segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva", "Tactil"))
  if modo =="visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "tactil":
    st.write("El tacto es fundamental para tu interfaz")
    
with st.sidebar:
  st.subheader("Configure la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("visual", "auditiva", "haptica")
)
    
