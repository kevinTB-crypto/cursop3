import streamlit as st
import google.generativeai as genai


def generate_course(text):

    api_key = st.secrets["GEMINI_API_KEY"]

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Convierte la siguiente transcripción en un curso MOOC profesional.

Genera:

# Título

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

## Resumen

## Examen Final

Genera 10 preguntas de opción múltiple con respuesta correcta.

TRANSCRIPCIÓN:

{text}
"""

    response = model.generate_content(prompt)

    return response.text