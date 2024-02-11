import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from core.utils.identifiers import generate_uuid


class Base(AsyncAttrs, DeclarativeBase):
    pass


class BaseModel:
    id = Column(
        String,
        primary_key=True,
        default=generate_uuid,
        index=True,
        nullable=False,
    )
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(
        DateTime(timezone=True), onupdate=datetime.datetime.now
    )
