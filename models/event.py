import uuid
from sqlalchemy import Column, String, Integer
from database.base import Base
from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = "events"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_type = Column(String(100))
    risk_score = Column(Integer)
    status = Column(String(50))
   # evidences = relationship(
    #    "Evidence",
     #   back_populates="event"
    #)

    #alerts = relationship(
     #   "Alert",
      #  back_populates="event"
    #)