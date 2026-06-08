import sqlite3


def init_db():

    conn = sqlite3.connect(
        "students.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_name TEXT,

        course_name TEXT,

        percentage REAL
    )
    """)

    conn.commit()

    conn.close()


def save_progress(
    student_name,
    course_name,
    percentage
):

    conn = sqlite3.connect(
        "students.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO progress
    (
        student_name,
        course_name,
        percentage
    )
    VALUES
    (?, ?, ?)
    """,
    (
        student_name,
        course_name,
        percentage
    ))

    conn.commit()

    conn.close()