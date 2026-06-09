from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.evidence import Evidence

Session = sessionmaker(bind=engine)


def create_evidence(
        event_id,
        photo_path,
        video_path,
        audio_path):

    session = Session()

    evidence = Evidence(
        event_id=event_id,
        photo_path=photo_path,
        video_path=video_path,
        audio_path=audio_path
    )

    session.add(evidence)
    session.commit()

    print("Evidence Saved")

    session.close()