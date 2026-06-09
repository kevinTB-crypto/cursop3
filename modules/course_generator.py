import streamlit as st
import google.generativeai as genai


def generate_course(text):

    genai.configure(
        api_key=st.secrets[
            "GEMINI_API_KEY"
        ]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Convierte esta transcripción en un curso MOOC.

Incluye:

# Título

## Descripción

## Objetivos

## Módulo 1

## Módulo 2

## Módulo 3

## Actividades

## Resumen

Transcripción:

{text}
"""

    response = model.generate_content(
        prompt
    )

    return response.text