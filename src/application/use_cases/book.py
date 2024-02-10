from typing import List

from application.interfaces.author_repository import AuthorRepository
from application.interfaces.book_repository import BookRepository
from application.interfaces.publisher import BaseEventPublisher
from application.use_cases.author import AuthorUseCases
from domain.entities.book import Book as BookEntity
from domain.events.book_created import BookCreatedEvent
from domain.events.book_deleted import BookDeletedEvent
from domain.events.book_updated import BookUpdatedEvent


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
        event_publisher: BaseEventPublisher,
    ) -> BookEntity:
        author = AuthorUseCases.get_or_create_author(
            name=author_name,
            author_repository=author_repository,
            event_publisher=event_publisher,
        )
        book = BookEntity(title=title, author=author)

        new_book = book_repository.create_book(book)

        book_created_event = BookCreatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        event_publisher.publish_event(book_created_event)

        return new_book

    @staticmethod
    def update_book(
        book_id: str,
        title: str,
        author_name: str,
        book_repository: BookRepository,
        author_repository: AuthorRepository,
        event_publisher: BaseEventPublisher,
    ) -> BookEntity:
        author = AuthorUseCases.get_or_create_author(
            name=author_name,
            author_repository=author_repository,
            event_publisher=event_publisher,
        )

        book = BookEntity(id=book_id, title=title, author=author)
        new_book = book_repository.update_book(book)

        book_updated = BookUpdatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        event_publisher.publish_event(book_updated)

        return new_book

    @staticmethod
    def delete_book(
        book_id: str,
        book_repository: BookRepository,
        event_publisher: BaseEventPublisher,
    ) -> None:
        book_repository.delete_book(book_id)

        book_deleted_event = BookDeletedEvent(book_id=book_id)
        event_publisher.publish_event(book_deleted_event)
