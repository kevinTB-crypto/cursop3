import streamlit as st
from modules.transcript import get_transcript
from urllib.parse import urlparse, parse_qs

# Función para obtener el ID del video
def get_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    if "youtube.com" in url:
        return parse_qs(
            urlparse(url).query
        )["v"][0]

st.title("YouTube → Curso IA")

url = st.text_input("URL de YouTube")

if st.button("Generar Curso"):

    video_id = get_video_id(url)
    try:
        transcript = get_transcript(video_id)

        st.success("Transcripción obtenida")
        st.write(transcript[:1000])
    except Exception as e:
        st.error(f"No se pudo obtener la transcripción.\n\n{e}")