from typing import List

from common.interfaces.publisher import BaseEventPublisher
from core.domain.entities.book import Book as BookEntity
from core.use_cases.book import BookUseCases
from external.database.sqlalchemy.repositories.author import AuthorRepository
from external.database.sqlalchemy.repositories.books import BookRepository


class BookController:
    @staticmethod
    def get_books() -> List[BookEntity]:
        book_repository = BookRepository()
        return BookUseCases.get_books(book_repository=book_repository)

    @staticmethod
    def get_book(book_id: str) -> BookEntity:
        book_repository = BookRepository()
        return BookUseCases.get_book(
            book_id=book_id, book_repository=book_repository
        )

    @staticmethod
    def create_book(
        title: str, author_name: str, event_publisher: BaseEventPublisher
    ) -> BookEntity:
        book_repository = BookRepository()
        author_repository = AuthorRepository()
        return BookUseCases.create_book(
            title=title,
            author_name=author_name,
            book_repository=book_repository,
            author_repository=author_repository,
            event_publisher=event_publisher,
        )

    @staticmethod
    def update_book(
        book_id: str,
        title: str,
        author_name: str,
        event_publisher: BaseEventPublisher,
    ) -> BookEntity:
        book_repository = BookRepository()
        author_repository = AuthorRepository()
        BookUseCases.update_book(
            book_id=book_id,
            title=title,
            author_name=author_name,
            book_repository=book_repository,
            author_repository=author_repository,
            event_publisher=event_publisher,
        )

    @staticmethod
    def delete_book(book_id: str, event_publisher: BaseEventPublisher) -> None:
        book_repository = BookRepository()
        BookUseCases.delete_book(
            book_id=book_id,
            book_repository=book_repository,
            event_publisher=event_publisher,
        )
