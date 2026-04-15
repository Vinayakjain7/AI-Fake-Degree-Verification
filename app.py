from flask import Flask, render_template, request, send_file
import os
import json
import csv
from werkzeug.utils import secure_filename

from ocr_module import process_certificate
from logger import log_verification

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
LOG_FILE = "verification_log.json"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------------------
# HOME
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# VERIFY CERTIFICATE
# ---------------------------
@app.route("/verify", methods=["POST"])
def verify():

    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]

    if file.filename == "":
        return "No selected file."

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(file_path)

    result = process_certificate(file_path)

    if "error" in result:
        return result["error"]

    log_verification(
        filename=filename,
        status=result["status"],
        score=result["final_score"],
        db_verified=result["verified"],
        tampering_score=result["tampering_score"]
    )

    return render_template(
        "result.html",
        extracted_data=result["extracted_data"],
        verified=result["verified"],
        tampering_score=result["tampering_score"],
        final_score=result["final_score"],
        status=result["status"],
        remarks=result["remarks"],
        ela_image=result["ela_image"],
        score_width=str(result["final_score"]) + "%"
    )


# ---------------------------
# ADMIN DASHBOARD
# ---------------------------
@app.route("/admin")
def admin_dashboard():

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    total = len(logs)
    authentic = sum(1 for log in logs if log["status"] == "Highly Authentic")
    suspicious = sum(1 for log in logs if log["status"] == "Suspicious")

    success_rate = round((authentic / total) * 100, 2) if total > 0 else 0

    return render_template(
        "admin.html",
        logs=logs[::-1],
        total=total,
        authentic=authentic,
        suspicious=suspicious,
        success_rate=success_rate
    )


# ---------------------------
# EXPORT CSV
# ---------------------------
@app.route("/export-csv")
def export_csv():

    if not os.path.exists(LOG_FILE):
        return "No logs available."

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    csv_filename = "verification_report.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Filename",
            "Status",
            "Score",
            "Database Verified",
            "Tampering Score",
            "Timestamp"
        ])

        for log in logs:
            writer.writerow([
                log["filename"],
                log["status"],
                log["score"],
                log["database_verified"],
                log["tampering_score"],
                log["timestamp"]
            ])

    return send_file(csv_filename, as_attachment=True)


# ---------------------------
# RUN APP (RENDER FIX)
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)