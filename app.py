import streamlit as st
from modules.transcript import get_transcript
from urllib.parse import urlparse, parse_qs


def get_video_id(url):
    try:
        if "youtu.be" in url:
            return url.split("/")[-1].split("?")[0]

        if "youtube.com" in url:
            query = parse_qs(urlparse(url).query)
            return query.get("v", [None])[0]

        return None
    except:
        return None


st.title("YouTube → Curso IA")

url = st.text_input("URL de YouTube")

if st.button("Generar Curso"):

    if  not url:
        st.error("Ingresa una URL.")
        st.stop()

    video_id = get_video_id(url)

    if not video_id:
        st.error("URL de YouTube no válida.")
        st.stop()

    try:
        transcript = get_transcript(video_id)

        st.success("Transcripción obtenida")
        st.write(transcript[:1000])

    except Exception as e:
        st.error(f"No se pudo obtener la transcripción.\n\n{e}")