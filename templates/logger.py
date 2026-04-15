import json
import os
from datetime import datetime

LOG_FILE = "verification_log.json"


def log_verification(filename, status, score, db_verified, tampering_score):

    log_entry = {
        "filename": filename,
        "status": status,
        "score": score,
        "database_verified": db_verified,
        "tampering_score": tampering_score,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)