from typing import List, Union

from common.interfaces.book_gateway import BookGatewayInterface
from common.interfaces.book_repository import BookRepositoryInterface
from core.domain.entities.book import Book as BookEntity


class BookGateway(BookGatewayInterface):
    def __init__(self, book_repository: BookRepositoryInterface):
        self.book_repository = book_repository

    async def create_book(self, book: BookEntity) -> BookEntity:
        return await self.book_repository.create_book(book=book)

    async def get_books(self) -> List[BookEntity]:
        return await self.book_repository.get_books()

    async def get_book(self, book_id: int) -> BookEntity:
        return await self.book_repository.get_book(book_id=book_id)

    async def update_book(self, book: BookEntity) -> Union[BookEntity, None]:
        return await self.book_repository.update_book(book=book)

    async def delete_book(self, book_id: int) -> None:
        await self.book_repository.delete_book(book_id=book_id)
