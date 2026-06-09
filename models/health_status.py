import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func

from database.base import Base


class HealthStatus(Base):

    __tablename__ = "health_status"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    camera_status = Column(String(20))

    microphone_status = Column(String(20))

    database_status = Column(String(20))

    internet_status = Column(String(20))

    service_status = Column(String(20))

    updated_at = Column(
        DateTime,
        server_default=func.now()
    )