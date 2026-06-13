from flask import Blueprint, jsonify
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.event import Event
from models.evidence import Evidence

event_details_bp = Blueprint(
    "event_details",
    __name__
)

Session = sessionmaker(bind=engine)


@event_details_bp.route(
    "/event/<event_id>",
    methods=["GET"]
)
def get_event_details(event_id):

    session = Session()

    try:

        event = session.query(Event).filter(
            Event.id == event_id
        ).first()

        evidence = session.query(Evidence).filter(
            Evidence.event_id == event_id
        ).first()

        if not event or not evidence:

            return jsonify({
                "success": False,
                "message": "Event not found"
            }), 404

        return jsonify({

            "success": True,

            "event_id": event.id,

            "event_type": event.event_type,

            "risk_score": event.risk_score,

            "risk_level": event.status,

            "photo_path": evidence.photo_path.replace("\\", "/"),
            "video_path": evidence.video_path.replace("\\", "/"),
            "audio_path": evidence.audio_path.replace("\\", "/")
        })

    finally:

        session.close()