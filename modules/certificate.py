from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_certificate(
    student_name,
    course_name,
    percentage,
    filename="certificado.pdf"
):

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CERTIFICADO DE APROBACIÓN",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Otorgado a: <b>{student_name}</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            f"Curso: {course_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Calificación: {percentage}%",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Felicidades por completar el curso.",
            styles["Normal"]
        )
    )

    pdf.build(content)

    return filename