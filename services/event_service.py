from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.event import Event

Session = sessionmaker(bind=engine)


def create_event(
    event_id,
    event_type,
    risk_score,
    status
):

    session = Session()

    try:

        event = Event(
            id=event_id,
            event_type=event_type,
            risk_score=risk_score,
            status=status
        )

        session.add(event)
        session.commit()

        print("Event Created")

        # Return the ID that was passed in
        return event_id

    finally:

        session.close()