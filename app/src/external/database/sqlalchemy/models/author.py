from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.external.database.sqlalchemy.models.base import Base, BaseModel


class Author(Base, BaseModel):
    __tablename__ = "authors"

    name = Column(
        String,
        index=True,
        unique=True,
        nullable=False,
    )
    books = relationship("Book", back_populates="author")
