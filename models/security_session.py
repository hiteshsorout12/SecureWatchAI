from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from datetime import datetime

from database.base import Base


class SecuritySession(Base):

    __tablename__ = "security_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_type = Column(
        String,
        default="NORMAL"
    )

    active = Column(
        Boolean,
        default=False
    )

    status = Column(
        String,
        default="NORMAL"
    )

    risk_score = Column(
        Integer,
        default=0
    )

    camera_on = Column(
        Boolean,
        default=False
    )

    microphone_on = Column(
        Boolean,
        default=False
    )

    live_stream_on = Column(
        Boolean,
        default=False
    )

    owner_connected = Column(
        Boolean,
        default=False
    )

    photo_path = Column(
        String,
        default=""
    )

    video_path = Column(
        String,
        default=""
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    ended_at = Column(
        DateTime,
        nullable=True
    )