from typing import List, Union

from sqlalchemy.orm.exc import NoResultFound

from core.domain.entities.book import Book as BookEntity
from external.database.sqlalchemy.mappers.book import BookMapper
from external.database.sqlalchemy.models.book import Book as BookModel
from external.database.sqlalchemy.session_mixing import use_database_session


class BookRepository:
    def create_book(self, book: BookEntity) -> BookEntity:
        with use_database_session() as db:
            book_model = BookMapper.entity_to_model(book)
            db.add(book_model)
            db.commit()
            db.refresh(book_model)
            return BookMapper.model_to_entity(book_model)

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

    def update_book(self, book: BookEntity) -> Union[BookEntity, None]:
        with use_database_session() as db:
            book_model = db.query(BookModel).filter_by(id=book.id).first()
            if book_model:
                book_model.title = book.title
                book_model.author_id = book.author.id
                db.commit()
                db.refresh(book_model)
                return BookMapper.model_to_entity(book_model)
            else:
                raise NoResultFound("Book not found")

    def delete_book(self, book_id: int) -> None:
        with use_database_session() as db:
            book = db.query(BookModel).filter_by(id=book_id).first()
            if book:
                db.delete(book)
                db.commit()
