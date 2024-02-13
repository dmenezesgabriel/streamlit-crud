from typing import Union

from src.communication.controllers.book import BookController
from src.external.database.sqlalchemy.repositories.author import \
    AuthorRepository
from src.external.database.sqlalchemy.repositories.book import BookRepository
from src.external.database.sqlalchemy.repositories.event import EventRepository


class SingletonBookController:
    _instance = None
    book_controller = None

    def __new__(cls) -> "SingletonBookController":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            book_repository = BookRepository()
            author_repository = AuthorRepository()
            event_repository = EventRepository()
            cls._instance.book_controller = BookController(
                book_repository=book_repository,
                author_repository=author_repository,
                event_repository=event_repository,
            )
        return cls._instance


def get_book_controller() -> Union[BookController, None]:
    return SingletonBookController().book_controller
