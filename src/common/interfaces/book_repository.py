from abc import ABC, abstractmethod
from typing import List, Union

from core.domain.entities.book import Book as BookEntity


class BookRepository(ABC):
    @abstractmethod
    def create_book(self, book: BookEntity) -> BookEntity:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> List[BookEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_book(self, book_id: int) -> BookEntity:
        raise NotImplementedError

    @abstractmethod
    def update_book(self, book: BookEntity) -> Union[BookEntity | None]:
        raise NotImplementedError

    @abstractmethod
    def delete_book(self, book_id: int) -> None:
        raise NotImplementedError
