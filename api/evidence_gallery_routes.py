from flask import Blueprint
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence
from models.event import Event

gallery_bp = Blueprint(
    "gallery",
    __name__
)

Session = sessionmaker(bind=engine)


@gallery_bp.route(
    "/evidence/all",
    methods=["GET"]
)
def get_all_evidence():

    session = Session()

    try:

        records = (
            session.query(Evidence, Event)
            .join(
                Event,
                Evidence.event_id == Event.id
            )
            .all()
        )

        result = []

        for evidence, event in records:

            result.append(
                {
                    "event_id": event.id,
                    "event_type": event.event_type,
                    "risk_score": event.risk_score,
                    "risk_level": event.status,

                    "photo_path": evidence.photo_path.replace("\\", "/"),
                    "video_path": evidence.video_path.replace("\\", "/"),
                    "audio_path": evidence.audio_path.replace("\\", "/")
                }
            )

        return result

    finally:

        session.close()