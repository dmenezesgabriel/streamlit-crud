from typing import List

from entities import Book as BookEntity
from repositories import BookRepository
from sqlalchemy.orm import Session


class BookService:
    def __init__(self, db: Session):
        self.book_repo = BookRepository(db)

    def create_book(self, title: str, author: str) -> BookEntity:
        return self.book_repo.create_book(title, author)

    def get_books(self) -> List[BookEntity]:
        return self.book_repo.get_books()

    def get_book(self, book_id: int) -> BookEntity:
        return self.book_repo.get_book(book_id)

    def update_book(self, book_id: int, title: str, author: str) -> BookEntity:
        return self.book_repo.update_book(book_id, title, author)

    def delete_book(self, book_id: int) -> BookEntity:
        return self.book_repo.delete_book(book_id)
