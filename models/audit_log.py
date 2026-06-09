import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import func

from database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    action = Column(String(100))

    module = Column(String(100))

    details = Column(Text)

    status = Column(String(50))

    created_at = Column(
        DateTime,
        server_default=func.now()
    )