from typing import List

from fastapi import APIRouter, HTTPException
from src.common.dto.book import BookDTO, EditBookDTO, NewBookDTO
from src.communication.controllers.book import BookController
from src.external.database.sqlalchemy.repositories.author import (
    AuthorRepository,
)
from src.external.database.sqlalchemy.repositories.book import BookRepository
from src.external.database.sqlalchemy.repositories.event import EventRepository

router = APIRouter(prefix="/books", tags=["books"])


author_repository = AuthorRepository()
book_repository = BookRepository()
event_repository = EventRepository()

book_controller = BookController(
    author_repository=author_repository,
    book_repository=book_repository,
    event_repository=event_repository,
)


@router.get("/", response_model=List[BookDTO])
async def read_books() -> List[BookDTO]:
    return [
        BookDTO(**book.to_dict()) for book in await book_controller.get_books()
    ]


@router.get("/{book_id}", response_model=BookDTO)
async def read_book(book_id: str) -> BookDTO:
    book = await book_controller.get_book(book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookDTO(**book.to_dict())


@router.post("/", response_model=BookDTO)
async def create_book(book: NewBookDTO) -> BookDTO:
    book = await book_controller.create_book(
        title=book.title, author_name=book.author.name
    )
    return BookDTO(**book.to_dict())


@router.put("/{book_id}", response_model=BookDTO)
async def update_book(book: EditBookDTO) -> BookDTO:
    book = await book_controller.update_book(
        book_id=book.id, title=book.title, author_name=book.author.name
    )
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookDTO(**book.to_dict())


@router.delete("/{book_id}")
async def delete_book(book_id: str) -> None:
    return await book_controller.delete_book(book_id=book_id)
