from sqlalchemy.orm import sessionmaker
from database.connection import engine
from models.event import Event

Session = sessionmaker(bind=engine)

session = Session()

event = Event(
    event_type="WAKE_EVENT",
    risk_score=10,
    status="ACTIVE"
)

session.add(event)
session.commit()

print("Event Inserted Successfully")