from typing import List

from common.interfaces.author_repository import AuthorRepository
from common.interfaces.book_repository import BookRepository
from core.domain.entities.book import Book as BookEntity
from core.domain.events.book_created import BookCreatedEvent
from core.domain.events.book_deleted import BookDeletedEvent
from core.domain.events.book_updated import BookUpdatedEvent
from core.use_cases.author import AuthorUseCases


class BookUseCases:
    @staticmethod
    def get_books(book_repository: BookRepository) -> List[BookEntity]:
        return book_repository.get_books()

    @staticmethod
    def get_book(book_id: str, book_repository: BookRepository) -> BookEntity:
        return book_repository.get_book(book_id)

    @staticmethod
    def create_book(
        title: str,
        author_name: str,
        book_repository: BookRepository,
        author_repository: AuthorRepository,
    ) -> BookEntity:
        author = AuthorUseCases.get_or_create_author(
            name=author_name,
            author_repository=author_repository,
        )
        book = BookEntity(title=title, author=author)

        new_book = book_repository.create_book(book)

        book_created_event = BookCreatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        return new_book

    @staticmethod
    def update_book(
        book_id: str,
        title: str,
        author_name: str,
        book_repository: BookRepository,
        author_repository: AuthorRepository,
    ) -> BookEntity:
        author = AuthorUseCases.get_or_create_author(
            name=author_name,
            author_repository=author_repository,
        )

        book = BookEntity(id=book_id, title=title, author=author)
        new_book = book_repository.update_book(book)

        book_updated = BookUpdatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        return new_book

    @staticmethod
    def delete_book(
        book_id: str,
        book_repository: BookRepository,
    ) -> None:
        book_repository.delete_book(book_id)

        book_deleted_event = BookDeletedEvent(book_id=book_id)
