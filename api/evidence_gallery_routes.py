from flask import Blueprint
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

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

        evidences = (
            session.query(Evidence)
            .all()
        )

        result = []

        for evidence in evidences:

            result.append(
                {
                    "event_id": evidence.event_id,
                    "photo_path": evidence.photo_path,
                    "video_path": evidence.video_path,
                    "audio_path": evidence.audio_path
                }
            )

        return result

    finally:
        session.close()