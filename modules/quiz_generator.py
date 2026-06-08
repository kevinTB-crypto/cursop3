import streamlit as st
import google.generativeai as genai


def generate_quiz(course):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Basado en el siguiente curso genera un examen.

Genera exactamente 10 preguntas.

Formato:

1. Pregunta

A) ...
B) ...
C) ...
D) ...

Respuesta Correcta: A

CURSO:

{course}
"""

    response = model.generate_content(
        prompt
    )

    return response.text