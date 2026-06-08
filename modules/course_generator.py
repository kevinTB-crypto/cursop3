import google.generativeai as genai

def generate_course(text):

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
    Convierte esta transcripción en un curso.

    Genera:

    - título
    - descripción
    - módulos
    - lecciones
    - examen final

    Transcripción:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text