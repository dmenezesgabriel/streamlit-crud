import sys

sys.path.append("src")

from external.database.sqlalchemy.models.author import Author
from external.database.sqlalchemy.models.book import Book
from external.database.sqlalchemy.models.event import Event
from external.database.sqlalchemy.orm import Base, engine

Base.metadata.create_all(bind=engine)
