import streamlit as st
import google.generativeai as genai


def generate_quiz(course):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    prompt = f"""
Genera un examen de 10 preguntas
de opción múltiple basado en este curso.

Incluye:

Pregunta
A)
B)
C)
D)

Y marca la respuesta correcta.

CURSO:

{course}
"""

    response = model.generate_content(
        prompt
    )

    return response.text