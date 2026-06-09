import streamlit as st

from modules.transcript import (
    transcribe_file,
    transcribe_youtube
)

from modules.course_generator import (
    generate_course
)

st.set_page_config(
    page_title="MOOC IA",
    page_icon="🎓"
)

st.title(
    "🎓 Generador de Cursos MOOC"
)

modo = st.radio(
    "Origen del contenido",
    [
        "YouTube",
        "Archivo MP4"
    ]
)

transcript = None

if modo == "YouTube":

    url = st.text_input(
        "URL de YouTube"
    )

    if st.button(
        "Generar Curso"
    ):

        try:

            with st.spinner(
                "Transcribiendo video..."
            ):

                transcript = (
                    transcribe_youtube(
                        url
                    )
                )

            with st.spinner(
                "Generando curso..."
            ):

                course = (
                    generate_course(
                        transcript
                    )
                )

            st.success(
                "Curso generado"
            )

            st.markdown(
                course
            )

        except Exception as e:

            st.error(
                str(e)
            )

else:

    uploaded_file = st.file_uploader(
        "Sube un MP4",
        type=["mp4"]
    )

    if (
        uploaded_file
        and st.button(
            "Generar Curso"
        )
    ):

        try:

            temp_path = (
                f"/tmp/{uploaded_file.name}"
            )

            with open(
                temp_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            with st.spinner(
                "Transcribiendo..."
            ):

                transcript = (
                    transcribe_file(
                        temp_path
                    )
                )

            with st.spinner(
                "Generando curso..."
            ):

                course = (
                    generate_course(
                        transcript
                    )
                )

            st.success(
                "Curso generado"
            )

            st.markdown(
                course
            )

        except Exception as e:

            st.error(
                str(e)
            )