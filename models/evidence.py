import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func

from database.base import Base


class Evidence(Base):

    __tablename__ = "evidence"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_id = Column(String)

    photo_path = Column(String(500))

    video_path = Column(String(500))

    audio_path = Column(String(500))

    encrypted = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )