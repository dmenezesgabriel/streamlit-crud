from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from infrastructure.database.sqlalchemy.orm import Base
from utils.identifiers import generate_uuid


class Author(Base):
    __tablename__ = "authors"
    id = Column(
        String,
        primary_key=True,
        default=generate_uuid,
        index=True,
        nullable=False,
    )
    name = Column(
        String,
        index=True,
        unique=True,
        nullable=False,
    )
    books = relationship("Book", back_populates="author")
