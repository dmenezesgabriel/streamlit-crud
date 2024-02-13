from abc import ABC, abstractmethod
from typing import List, Union

from src.core.domain.entities.book import Book as BookEntity


class BookGatewayInterface(ABC):
    @abstractmethod
    async def create_book(self, book: BookEntity) -> BookEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_books(self) -> List[BookEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_book(self, book_id: str) -> BookEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_book_by_title_and_author_id(
        self, title: str, author_id: str
    ) -> Union[BookEntity, None]:
        raise NotImplementedError

    @abstractmethod
    async def update_book(self, book: BookEntity) -> Union[BookEntity | None]:
        raise NotImplementedError

    @abstractmethod
    async def delete_book(self, book_id: str) -> None:
        raise NotImplementedError
