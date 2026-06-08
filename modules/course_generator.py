import os
import google.generativeai as genai


def generate_course(text):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise Exception(
            "No se encontró GEMINI_API_KEY"
        )

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Convierte la siguiente transcripción en un curso MOOC profesional.

Genera en formato Markdown:

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

Indica la respuesta correcta.

TRANSCRIPCIÓN:

{text}
"""

    response = model.generate_content(prompt)

    return response.text