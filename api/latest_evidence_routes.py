from flask import Blueprint
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

latest_evidence_bp = Blueprint(
    "latest_evidence",
    __name__
)

Session = sessionmaker(bind=engine)


@latest_evidence_bp.route(
    "/evidence/latest",
    methods=["GET"]
)
def get_latest_evidence():

    session = Session()

    try:

        evidence = (
            session.query(Evidence)
            .order_by(
                desc(Evidence.created_at)
            )
            .first()
        )

        if not evidence:

            return {
                "message": "No Evidence Found"
            }

        return {
            "event_id": evidence.event_id,
            "photo_path": evidence.photo_path.replace("\\", "/"),
            "video_path": evidence.video_path.replace("\\", "/"),
            "audio_path": evidence.audio_path.replace("\\", "/")
        }

    finally:
        session.close()