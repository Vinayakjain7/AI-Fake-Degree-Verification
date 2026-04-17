import sqlite3


def verify_certificate(text):

    conn = sqlite3.connect("certificates.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM certificates")
    records = cursor.fetchall()

    conn.close()

    text = text.lower()

    best_score = 0
    verified = False

    for record in records:
        name = record[0].lower()
        university = record[1].lower()
        year = str(record[2])

        score = 0

        if name in text:
            score += 0.4
        if university in text:
            score += 0.4
        if year in text:
            score += 0.2

        best_score = max(best_score, score)

    if best_score >= 0.6:
        verified = True

    return verified, best_score, None
