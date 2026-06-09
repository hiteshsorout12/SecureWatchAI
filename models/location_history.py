import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from database.base import Base

from datetime import datetime


class LocationHistory(Base):

    __tablename__ = "location_history"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    device_name = Column(String(100))

    latitude = Column(String(100))

    longitude = Column(String(100))

    timestamp = Column(
        DateTime,
        default=datetime.now
    )