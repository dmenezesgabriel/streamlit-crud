from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from src.external.database.sqlalchemy.models.base import Base, BaseModel


class Book(Base, BaseModel):
    __tablename__ = "books"
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
    author = relationship("Author", lazy="select")

    # Unique constraint on the combination of author and book title
    __table_args__ = (
        UniqueConstraint("title", "author_id", name="_title_author_uc"),
    )
