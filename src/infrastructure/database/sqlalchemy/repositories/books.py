from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from domain.entities.author import Author as AuthorEntity
from domain.entities.book import Book as BookEntity
from infrastructure.database.sqlalchemy.mappers.author import AuthorMapper
from infrastructure.database.sqlalchemy.mappers.book import BookMapper
from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)
from infrastructure.database.sqlalchemy.models.book import Book


class AuthorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_author_by_name(self, name: str) -> AuthorEntity:
        author = self.db.query(AuthorModel).filter_by(name=name).first()
        if author:
            return AuthorMapper.model_to_entity(author)
        else:
            return None

    def create_author(self, name: str) -> AuthorEntity:
        try:
            author = AuthorModel(name=name)
            self.db.add(author)
            self.db.commit()
            self.db.refresh(author)
            return AuthorMapper.model_to_entity(author)
        except Exception as error:
            self.db.rollback()
            raise error


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, title: str, author_name: str):
        try:
            # Check if the author already exists
            existing_author = (
                self.db.query(AuthorModel).filter_by(name=author_name).first()
            )

            if existing_author:
                # Use the existing author
                author = existing_author
            else:
                # Create a new author
                author = AuthorModel(name=author_name)
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
                self.db.query(AuthorModel).filter_by(name=author_name).first()
            )

            if existing_author:
                # Use the existing author
                book.author = existing_author
            else:
                # Create a new author and assign to the book
                new_author = AuthorModel(name=author_name)
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
