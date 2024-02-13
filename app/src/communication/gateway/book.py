from typing import List, Union

from src.common.interfaces.book_gateway import BookGatewayInterface
from src.common.interfaces.book_repository import BookRepositoryInterface
from src.core.domain.entities.book import Book as BookEntity


class BookGateway(BookGatewayInterface):
    def __init__(self, book_repository: BookRepositoryInterface):
        self.book_repository = book_repository

    async def create_book(self, book: BookEntity) -> BookEntity:
        return await self.book_repository.create_book(book=book)

    async def get_books(self) -> List[BookEntity]:
        return await self.book_repository.get_books()

    async def get_book(self, book_id: str) -> BookEntity:
        return await self.book_repository.get_book(book_id=book_id)

    async def get_book_by_title_and_author_id(
        self, title: str, author_id: str
    ) -> Union[BookEntity, None]:
        return await self.book_repository.get_book_by_title_and_author_id(
            title=title, author_id=author_id
        )

    async def update_book(self, book: BookEntity) -> Union[BookEntity, None]:
        return await self.book_repository.update_book(book=book)

    async def delete_book(self, book_id: str) -> None:
        await self.book_repository.delete_book(book_id=book_id)
