import sqlite3
from difflib import SequenceMatcher


def normalize(text):
    if not text:
        return ""
    return " ".join(text.lower().strip().split())


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def create_database():
    conn = sqlite3.connect("certificates.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            filename TEXT,
            nome TEXT,
            curso TEXT,
            universidade TEXT,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_certificate(filename, nome, curso, universidade, data):
    conn = sqlite3.connect("certificates.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO certificates VALUES (?, ?, ?, ?, ?)
    """, (
        filename,
        normalize(nome),
        normalize(curso),
        normalize(universidade),
        normalize(data)
    ))

    conn.commit()
    conn.close()


def verify_certificate(extracted_data):
    conn = sqlite3.connect("certificates.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM certificates")
    records = cursor.fetchall()

    conn.close()

    ext_nome = normalize(extracted_data.get("Student Name", ""))
    ext_curso = normalize(extracted_data.get("Course", ""))
    ext_uni = normalize(extracted_data.get("University", ""))
    ext_data = normalize(extracted_data.get("Issue Date", ""))

    for record in records:
        _, db_nome, db_curso, db_uni, db_data = record

        if (
            similarity(ext_nome, db_nome) > 0.8 and
            similarity(ext_curso, db_curso) > 0.8 and
            similarity(ext_uni, db_uni) > 0.7 and
            similarity(ext_data, db_data) > 0.6
        ):
            return True

    return False
