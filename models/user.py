import uuid
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import relationship
from database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(String(100))

    email = Column(String(100))

    role = Column(String(50))

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    