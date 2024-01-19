from typing import List

from domain.entities.book import Book as BookEntity
from infrastructure.database.sqlalchemy.repositories.author import (
    AuthorRepository,
)
from infrastructure.database.sqlalchemy.repositories.books import (
    BookRepository,
)


class BookService:
    def __init__(self):
        self.book_repository = BookRepository()
        self.author_repository = AuthorRepository()

    def create_book(self, title: str, author_name: str) -> BookEntity:
        existing_author = self.author_repository.get_author_by_name(
            author_name
        )

        if existing_author:
            author = existing_author
        else:
            author = self.author_repository.create_author(author_name)

        return self.book_repository.create_book(title, author)

    def get_books(self) -> List[BookEntity]:
        return self.book_repository.get_books()

    def get_book(self, book_id: int) -> BookEntity:
        return self.book_repository.get_book(book_id)

    def update_book(
        self, book_id: int, title: str, author_name: str
    ) -> BookEntity:
        existing_author = self.author_repository.get_author_by_name(
            author_name
        )

        if existing_author:
            author = existing_author
        else:
            author = self.author_repository.create_author(author_name)
        return self.book_repository.update_book(book_id, title, author)

    def delete_book(self, book_id: int) -> BookEntity:
        return self.book_repository.delete_book(book_id)
