import sys

sys.path.append("src")

from infrastructure.database.sqlalchemy.models.author import Author
from infrastructure.database.sqlalchemy.models.book import Book
from infrastructure.database.sqlalchemy.orm import Base, engine

Base.metadata.create_all(bind=engine)
