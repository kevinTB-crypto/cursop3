import streamlit as st
import google.generativeai as genai


def generate_course(text):

    try:

        api_key = st.secrets["GEMINI_API_KEY"]

        genai.configure(
            api_key=api_key
        )

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        prompt = f"""
Convierte la siguiente transcripción en un curso MOOC profesional.

Genera el resultado en formato Markdown.

Incluye:

# Título del Curso

## Descripción

## Objetivos de Aprendizaje

## Módulo 1
### Lección 1
### Lección 2

## Módulo 2
### Lección 1
### Lección 2

## Módulo 3
### Lección 1
### Lección 2

## Actividades Prácticas

## Resumen General

## Examen Final

Genera 10 preguntas de opción múltiple.

Cada pregunta debe tener:

A)
B)
C)
D)

Indica claramente la respuesta correcta.

TRANSCRIPCIÓN:

{text}
"""

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        if "429" in str(e):

            return """
# Límite alcanzado

Has alcanzado temporalmente el límite gratuito de Gemini.

Espera aproximadamente 1 minuto y vuelve a intentarlo.
"""

        if "GEMINI_API_KEY" in str(e):

            return """
# Error de configuración

No se encontró la variable GEMINI_API_KEY en Streamlit Secrets.
"""

        return f"""
# Error

Se produjo un error:

{str(e)}
"""