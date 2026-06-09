from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.event import Event

Session = sessionmaker(bind=engine)


def create_event(event_type,
                 risk_score,
                 status):

    session = Session()

    event = Event(
        event_type=event_type,
        risk_score=risk_score,
        status=status
    )

    session.add(event)

    session.commit()

    event_id = event.id

    print("Event Created")

    session.close()

    return event_id