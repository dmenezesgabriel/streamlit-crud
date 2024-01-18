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
            author = Author(name=author_name)
            book = Book(title=title, author=author)
            self.db.add(author)
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
            book.author.name = author_name
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
