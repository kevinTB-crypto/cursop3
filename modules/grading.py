def calculate_grade(score, total):

    percentage = round(
        (score / total) * 100,
        2
    )

    if percentage >= 70:
        status = "Aprobado"
    else:
        status = "Reprobado"

    return {
        "score": score,
        "total": total,
        "percentage": percentage,
        "status": status
    }