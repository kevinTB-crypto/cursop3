import streamlit as st
from urllib.parse import urlparse, parse_qs

from modules.transcript import get_transcript
from modules.course_generator import generate_course

st.set_page_config(
    page_title="YouTube → Curso IA",
    page_icon="🎓",
    layout="wide"
)


def get_video_id(url):
    try:
        if "youtu.be" in url:
            return url.split("/")[-1].split("?")[0]

        if "youtube.com" in url:
            query = parse_qs(urlparse(url).query)
            return query.get("v", [None])[0]

        return None

    except Exception:
        return None


st.title("🎓 Generador de Cursos MOOC con IA")

url = st.text_input(
    "URL de YouTube",
    placeholder="https://youtube.com/watch?v=..."
)

if st.button("Generar Curso"):

    if not url:
        st.error("Ingresa una URL.")
        st.stop()

    video_id = get_video_id(url)

    if not video_id:
        st.error("URL de YouTube no válida.")
        st.stop()

    try:

        # TEMPORAL
        # Cuando arreglemos transcript.py,
        # cambia esta parte por:
        #
        # transcript = get_transcript(video_id)

        transcript = """
        Python es un lenguaje de programación.
        Las variables almacenan datos.
        Las funciones permiten reutilizar código.
        Los ciclos permiten repetir instrucciones.
        """

        with st.spinner("Generando curso con IA..."):
            course = generate_course(transcript)

        st.success("Curso generado correctamente")
        st.markdown(course)

    except Exception as e:

        if "429" in str(e):
            st.warning(
                "Se alcanzó el límite de Gemini. Espera aproximadamente 1 minuto y vuelve a intentarlo."
            )
        else:
            st.error(f"Error:\n\n{e}")