import uuid

from db import Base
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship


def generate_uuid():
    return str(uuid.uuid4())


class Book(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    title = Column(String, index=True)
    author_id = Column(String, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")

    # Unique constraint on the combination of author and book title
    __table_args__ = (
        UniqueConstraint("title", "author_id", name="_title_author_uc"),
    )
