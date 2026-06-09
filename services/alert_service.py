from sqlalchemy.orm import sessionmaker

from database.connection import engine
from models.alert import Alert

Session = sessionmaker(bind=engine)


def create_alert(
        event_id,
        channel):

    session = Session()

    alert = Alert(
        event_id=event_id,
        channel=channel,
        sent_status=False
    )

    session.add(alert)
    session.commit()

    print("Alert Created")

    session.close()