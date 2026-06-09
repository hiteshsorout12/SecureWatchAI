import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from database.base import Base

from datetime import datetime


class DeviceStatus(Base):

    __tablename__ = "device_status"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    device_name = Column(String(100))

    ip_address = Column(String(100))

    city = Column(String(100))

    country = Column(String(100))

    status = Column(String(50))

    latitude = Column(String(100))

    longitude = Column(String(100))

    wifi_name = Column(String(200))

    battery_percent = Column(String(50))

    last_seen = Column(
        DateTime,
        default=datetime.now
    )