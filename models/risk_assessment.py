import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func

from sqlalchemy.orm import relationship

from database.base import Base


class RiskAssessment(Base):

    __tablename__ = "risk_assessments"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_id = Column(
        String,
        ForeignKey("events.id")
    )

    face_score = Column(Integer, default=0)

    login_score = Column(Integer, default=0)

    tamper_score = Column(Integer, default=0)

    audio_score = Column(Integer, default=0)

    total_score = Column(Integer, default=0)

    risk_level = Column(String(20))

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    event = relationship("Event")