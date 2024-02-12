from typing import List

from fastapi import APIRouter, HTTPException

from communication.controllers.book import BookController
from core.domain.entities.book import Book as BookEntity
from external.database.sqlalchemy.repositories.author import AuthorRepository
from external.database.sqlalchemy.repositories.book import BookRepository
from external.database.sqlalchemy.repositories.event import EventRepository

router = APIRouter(prefix="/books", tags=["books"])


author_repository = AuthorRepository()
book_repository = BookRepository()
event_repository = EventRepository()

book_controller = BookController(
    author_repository=author_repository,
    book_repository=book_repository,
    event_repository=event_repository,
)


@router.get("/")
async def read_books():
    return [book.to_json() for book in await book_controller.get_books()]
