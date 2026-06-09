import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func
#from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_id = Column(String)

    channel = Column(String(50))

    sent_status = Column(Boolean, default=False)

    retry_count = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )