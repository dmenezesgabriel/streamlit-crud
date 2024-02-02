from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, String

from infrastructure.database.sqlalchemy.orm import Base
from utils.identifiers import generate_uuid


class Event(Base):
    __tablename__ = "events"
    id = Column(
        String,
        primary_key=True,
        default=generate_uuid,
        index=True,
        nullable=False,
    )
    event_type = Column(String(20), nullable=False)
    model_type = Column(String(20), nullable=False)
    model_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=True)
