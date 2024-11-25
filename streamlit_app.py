import streamlit as st

st.title("🎈 El blog de una principiante en Python")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


calificación = st.slider("¿Cómo calificarías tu experiencia aprendiendo a programar en Python?")

st.write(f"la calificación seleccionada es: {calificación} ⭐")
