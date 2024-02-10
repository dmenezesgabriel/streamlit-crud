from typing import List

from common.interfaces.author_repository import AuthorRepositoryInterface
from common.interfaces.book_repository import BookRepositoryInterface
from communication.gateway.author import AuthorGateway
from communication.gateway.book import BookGateway
from core.domain.entities.book import Book as BookEntity
from core.use_cases.book import BookUseCases


class BookController:
    def __init__(
        self,
        book_repository: BookRepositoryInterface,
        author_repository: AuthorRepositoryInterface,
    ):
        self.book_repository = book_repository
        self.author_repository = author_repository

    async def get_books(self) -> List[BookEntity]:
        book_gateway = BookGateway(self.book_repository)
        return await BookUseCases.get_books(book_gateway=book_gateway)

    async def get_book(self, book_id: str) -> BookEntity:
        book_gateway = BookGateway(self.book_repository)
        return await BookUseCases.get_book(
            book_id=book_id, book_gateway=book_gateway
        )

    async def create_book(self, title: str, author_name: str) -> BookEntity:
        book_gateway = BookGateway(self.book_repository)
        author_gateway = AuthorGateway(self.author_repository)
        return await BookUseCases.create_book(
            title=title,
            author_name=author_name,
            book_gateway=book_gateway,
            author_gateway=author_gateway,
        )

    async def update_book(
        self,
        book_id: str,
        title: str,
        author_name: str,
    ) -> BookEntity:
        book_gateway = BookGateway(self.book_repository)
        author_gateway = AuthorGateway(self.author_repository)
        await BookUseCases.update_book(
            book_id=book_id,
            title=title,
            author_name=author_name,
            book_gateway=book_gateway,
            author_gateway=author_gateway,
        )

    async def delete_book(self, book_id: str) -> None:
        book_gateway = BookGateway(self.book_repository)
        await BookUseCases.delete_book(
            book_id=book_id,
            book_gateway=book_gateway,
        )
