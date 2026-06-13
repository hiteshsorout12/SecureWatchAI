from sqlalchemy import Column, Integer, Boolean, String, DateTime

from database import Base

from datetime import datetime


class EmergencySession(Base):

    __tablename__ = "emergency_session"

    id = Column(
        Integer,
        primary_key=True
    )

    active = Column(
        Boolean,
        default=False
    )

    risk_score = Column(
        Integer,
        default=0
    )

    status = Column(
        String,
        default="NORMAL"
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    ended_at = Column(
        DateTime,
        nullable=True
    )

    photo = Column(
        String,
        default=""
    )

    video = Column(
        String,
        default=""
    )