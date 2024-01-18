from models import Author, Book
from sqlalchemy.orm import Session


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
            return book
        except Exception as error:
            self.db.rollback()
            raise error

    def get_books(self):
        return self.db.query(Book).all()

    def get_book(self, book_id: int):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def update_book(self, book_id: int, title: str, author_name: str):
        book = self.get_book(book_id)
        if book:
            book.title = title
            book.author.name = author_name
            self.db.commit()
            self.db.refresh(book)
        return book

    def delete_book(self, book_id: int):
        book = self.get_book(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
        return book
