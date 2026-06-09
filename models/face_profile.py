import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func

from sqlalchemy.orm import relationship

from database.base import Base


class FaceProfile(Base):

    __tablename__ = "face_profiles"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String,
        ForeignKey("users.id")
    )

    encoding = Column(String)

    threshold = Column(
        Float,
        default=0.60
    )

    last_seen = Column(DateTime)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    user = relationship(
        "User"
    )