def calculate_score(is_verified, tampering_score):

    score = 0
    remarks = []

    # Database Verification (VERY STRONG SIGNAL)
    if is_verified:
        score += 60
        remarks.append("Database Match ✔")
    else:
        score -= 40   # heavy penalty
        remarks.append("Database Mismatch ❌")

    # Tampering Detection
    if tampering_score < 8:
        score += 40
        remarks.append("No Significant Tampering ✔")
    elif tampering_score < 20:
        score += 10
        remarks.append("Possible Tampering ⚠")
    else:
        score -= 20
        remarks.append("High Tampering Detected ❌")

    # Final Classification
    if score >= 80:
        status = "Highly Authentic"
    elif score >= 40:
        status = "Likely Authentic"
    else:
        status = "Suspicious"

    return score, status, remarks
