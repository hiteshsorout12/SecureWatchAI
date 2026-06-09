from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.alert import Alert

alert_bp = Blueprint(
    "alerts",
    __name__
)

Session = sessionmaker(bind=engine)


@alert_bp.route("/alerts", methods=["GET"])
def get_alerts():

    session = Session()

    alerts = session.query(Alert).all()

    result = []

    for alert in alerts:

        result.append({
            "id": alert.id,
            "event_id": alert.event_id,
            "channel": alert.channel,
            "sent_status": alert.sent_status
        })

    session.close()

    return jsonify(result)


@alert_bp.route("/alerts", methods=["POST"])
def create_alert():

    data = request.get_json()

    session = Session()

    alert = Alert(
        event_id=data["event_id"],
        channel=data["channel"],
        sent_status=False
    )

    session.add(alert)
    session.commit()

    session.close()

    return jsonify({
        "message": "Alert Created Successfully"
    })