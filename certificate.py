from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def create_certificate(name):

    pdf = SimpleDocTemplate(
        f"certificates/{name}.pdf"
    )

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            "CERTIFICADO",
            styles["Title"]
        ),
        Spacer(1,20),
        Paragraph(
            f"Otorgado a {name}",
            styles["Heading2"]
        )
    ]

    pdf.build(content)