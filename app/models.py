import uuid

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Author(Base):
    __tablename__ = "authors"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    name = Column(String, index=True, unique=True)
    books = relationship("Book", back_populates="author")


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


# Create SQLite database engine
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
