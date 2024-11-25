import streamlit as st

st.title("El blog de una principiante en Python⛵")

st.write(
    "### Bienvenido viajero programador" )

st.write("Esta es una aplicación interactiva en donde puedes compartir con el mundo 🌎 tu experiencia aprendiendo el lenguaje de programación 'Python'")

calificación = st.slider("¿Cómo calificarías tu experiencia aprendiendo a programar en Python?")

st.write(f"la calificación seleccionada es: {calificación} ⭐")
