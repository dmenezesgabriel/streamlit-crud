from typing import List

from entities import Book as BookEntity
from mappers.book_mapper import BookMapper
from models import Author, Book
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, title: str, author_name: str):
        try:
            # Check if the author already exists
            existing_author = (
                self.db.query(Author).filter_by(name=author_name).first()
            )

            if existing_author:
                # Use the existing author
                author = existing_author
            else:
                # Create a new author
                author = Author(name=author_name)
                self.db.add(author)

            book = Book(title=title, author=author)
            self.db.add(book)
            self.db.commit()
            self.db.refresh(book)
            return BookMapper.model_to_entity(book)
        except Exception as error:
            self.db.rollback()
            raise error

    def get_books(self) -> List[BookEntity]:
        books = self.db.query(Book).all()
        return [BookMapper.model_to_entity(book) for book in books]

    def get_book(self, book_id: int) -> BookEntity:
        book = self.db.query(Book).filter_by(id=book_id).first()
        if book:
            return BookMapper.model_to_entity(book)
        else:
            raise NoResultFound("Book not found")

    def update_book(self, book_id: int, title: str, author_name: str):
        book = self.db.query(Book).filter_by(id=book_id).first()
        if book:
            book.title = title
            # Check if the author already exists
            existing_author = (
                self.db.query(Author).filter_by(name=author_name).first()
            )

            if existing_author:
                # Use the existing author
                book.author = existing_author
            else:
                # Create a new author and assign to the book
                new_author = Author(name=author_name)
                self.db.add(new_author)
                book.author = new_author

            self.db.commit()
            self.db.refresh(book)
            return BookMapper.model_to_entity(book)
        else:
            raise NoResultFound("Book not found")

    def delete_book(self, book_id: int):
        book = self.db.query(Book).filter_by(id=book_id).first()
        if book:
            self.db.delete(book)
            self.db.commit()
