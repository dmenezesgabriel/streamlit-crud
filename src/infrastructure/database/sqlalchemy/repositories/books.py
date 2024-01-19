from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from domain.entities.book import Book as BookEntity
from infrastructure.database.sqlalchemy.mappers.book import BookMapper
from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)
from infrastructure.database.sqlalchemy.models.book import Book


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, title: str, author: AuthorModel):
        try:
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

    def update_book(self, book_id: int, title: str, author: AuthorModel):
        book = self.db.query(Book).filter_by(id=book_id).first()
        if book:
            book.title = title
            book.author = author
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
