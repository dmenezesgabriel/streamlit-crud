from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from core.utils.identifiers import generate_uuid
from external.database.sqlalchemy.orm import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(
        String,
        primary_key=True,
        default=generate_uuid,
        index=True,
        nullable=False,
    )
    title = Column(
        String,
        index=True,
        nullable=False,
    )
    author_id = Column(
        String,
        ForeignKey("authors.id"),
        nullable=False,
    )
    author = relationship("Author", back_populates="books")

    # Unique constraint on the combination of author and book title
    __table_args__ = (
        UniqueConstraint("title", "author_id", name="_title_author_uc"),
    )
