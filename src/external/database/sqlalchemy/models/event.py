from sqlalchemy import JSON, Column, String

from core.utils.identifiers import generate_uuid
from external.database.sqlalchemy.orm import Base


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
