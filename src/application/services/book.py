from typing import List

from domain.entities.author import Author as AuthorEntity
from domain.entities.book import Book as BookEntity
from domain.events.book_created import BookCreatedEvent
from domain.events.book_deleted import BookDeletedEvent
from domain.events.book_updated import BookUpdatedEvent


class BookService:
    def __init__(self, book_repository, author_repository, event_publisher):
        self.book_repository = book_repository
        self.author_repository = author_repository
        self.event_publisher = event_publisher

    def create_book(self, title: str, author_name: str) -> BookEntity:
        existing_author = self.author_repository.get_author_by_name(
            author_name
        )

        if existing_author:
            author = existing_author
        else:
            new_author = AuthorEntity(name=author_name)
            author = self.author_repository.create_author(new_author)

        book = BookEntity(title=title, author=author)

        new_book = self.book_repository.create_book(book)

        book_created_event = BookCreatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        self.event_publisher.publish_event(book_created_event)

        return new_book

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
            new_author = AuthorEntity(name=author_name)
            author = self.author_repository.create_author(new_author)

        book = BookEntity(id=book_id, title=title, author=author)
        new_book = self.book_repository.update_book(book)

        book_updated = BookUpdatedEvent(
            book_id=book.id, title=book.title, author=book.author
        )
        self.event_publisher.publish_event(book_updated)

        return new_book

    def delete_book(self, book_id: int) -> BookEntity:
        self.book_repository.delete_book(book_id)

        book_deleted_event = BookDeletedEvent(book_id=book_id)
        self.event_publisher.publish_event(book_deleted_event)
