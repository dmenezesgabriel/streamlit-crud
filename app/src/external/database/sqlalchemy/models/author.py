from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from src.external.database.sqlalchemy.models.base import Base, BaseModel
from src.core.utils.identifiers import generate_uuid


class Author(Base, BaseModel):
    __tablename__ = "authors"

    name = Column(
        String,
        index=True,
        unique=True,
        nullable=False,
    )
    books = relationship("Book", back_populates="author")
