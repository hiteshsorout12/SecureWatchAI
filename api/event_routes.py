from flask import Blueprint
from flask import jsonify
from flask import request

from flask import send_file

from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.event import Event

event_bp = Blueprint(
    "events",
    __name__
)

Session = sessionmaker(bind=engine)


@event_bp.route("/events", methods=["GET"])
def get_events():

    session = Session()

    events = session.query(Event).all()

    result = []

    for event in events:

        result.append({
            "id": event.id,
            "event_type": event.event_type,
            "risk_score": event.risk_score,
            "status": event.status
        })

    session.close()

    return jsonify(result)


@event_bp.route("/events", methods=["POST"])
def create_event():

    data = request.get_json()

    session = Session()

    event = Event(
        event_type=data["event_type"],
        risk_score=data["risk_score"],
        status=data["status"]
    )

    session.add(event)
    session.commit()

    session.close()

    return jsonify({
        "message": "Event Created Successfully"
    })
    
