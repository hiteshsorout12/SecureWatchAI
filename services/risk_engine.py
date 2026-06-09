from datetime import datetime


def calculate_risk(
    failed_login=True,
    unknown_face=True,
    multiple_attempts=False
):

    risk_score = 0

    # Failed Login
    if failed_login:
        risk_score += 30

    # Unknown Face
    if unknown_face:
        risk_score += 40

    # Multiple Attempts
    if multiple_attempts:
        risk_score += 10

    # Night Detection
    current_hour = datetime.now().hour

    if (
        current_hour >= 23
        or
        current_hour <= 6
    ):
        risk_score += 20

    # Risk Level
    if risk_score >= 70:

        risk_level = "HIGH"

    elif risk_score >= 40:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }