from flask import Blueprint
from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

analytics_bp = Blueprint(
    "analytics",
    __name__
)

Session = sessionmaker(bind=engine)


@analytics_bp.route(
    "/analytics",
    methods=["GET"]
)
def analytics():

    session = Session()

    try:

        evidences = (
            session.query(Evidence)
            .all()
        )

        total_intrusions = len(evidences)

        photos = sum(
            1
            for e in evidences
            if e.photo_path
        )

        videos = sum(
            1
            for e in evidences
            if e.video_path
        )

        latest = (
            evidences[-1].created_at
            if evidences
            else None
        )

        return {
            "total_intrusions":
                total_intrusions,

            "photos":
                photos,

            "videos":
                videos,

            "last_detection": (
                latest.strftime(
                    "%d %b %Y, %I:%M %p"
                )
                if latest
                else "N/A"
            )
        }

    finally:
        session.close()