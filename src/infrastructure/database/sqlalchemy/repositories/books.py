from typing import List

from sqlalchemy.orm.exc import NoResultFound

from domain.entities.book import Book as BookEntity
from infrastructure.database.sqlalchemy.mappers.book import BookMapper
from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)
from infrastructure.database.sqlalchemy.models.book import Book as BookModel
from infrastructure.database.sqlalchemy.session_mixing import (
    use_database_session,
)


class BookRepository:
    def create_book(self, title: str, author: AuthorModel):
        with use_database_session() as db:
            book = BookModel(title=title, author=author)
            db.add(book)
            db.commit()
            db.refresh(book)
            return BookMapper.model_to_entity(book)

    def get_books(self) -> List[BookEntity]:
        with use_database_session() as db:
            books = db.query(BookModel).all()
            return [BookMapper.model_to_entity(book) for book in books]

    def get_book(self, book_id: int) -> BookEntity:
        with use_database_session() as db:
            book = db.query(BookModel).filter_by(id=book_id).first()
            if book:
                return BookMapper.model_to_entity(book)
            else:
                raise NoResultFound("Book not found")

    def update_book(self, book_id: int, title: str, author: AuthorModel):
        with use_database_session() as db:
            book = db.query(BookModel).filter_by(id=book_id).first()
            if book:
                book.title = title
                book.author = author
                db.commit()
                db.refresh(book)
                return BookMapper.model_to_entity(book)
            else:
                raise NoResultFound("Book not found")

    def delete_book(self, book_id: int):
        with use_database_session() as db:
            book = db.query(BookModel).filter_by(id=book_id).first()
            if book:
                db.delete(book)
                db.commit()
