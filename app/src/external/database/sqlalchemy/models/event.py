from sqlalchemy import JSON, Column, String
from src.external.database.sqlalchemy.models.base import Base, BaseModel


class Event(Base, BaseModel):
    __tablename__ = "events"
    event_type = Column(String(20), nullable=False)
    model_type = Column(String(20), nullable=False)
    model_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=True)
