from typing import List

from common.dto.book import BookDTO, NewBookDTO
from common.interfaces.author_gateway import AuthorGatewayInterface
from common.interfaces.book_gateway import BookGatewayInterface
from core.domain.entities.book import Book as BookEntity
from core.use_cases.author import AuthorUseCases


class BookUseCases:
    @staticmethod
    async def get_books(
        book_gateway: BookGatewayInterface,
    ) -> List[BookEntity]:
        return await book_gateway.get_books()

    @staticmethod
    async def get_book(
        book_id: str, book_gateway: BookGatewayInterface
    ) -> BookEntity:
        return await book_gateway.get_book(book_id)

    @staticmethod
    async def create_book(
        new_book_data: NewBookDTO,
        book_gateway: BookGatewayInterface,
        author_gateway: AuthorGatewayInterface,
    ) -> BookEntity:
        author = await AuthorUseCases.get_or_create_author(
            name=new_book_data.author.name,
            author_gateway=author_gateway,
        )
        book = BookEntity(title=new_book_data.title, author=author)

        new_book = await book_gateway.create_book(book)
        return new_book

    @staticmethod
    async def update_book(
        book_data: BookDTO,
        book_gateway: BookGatewayInterface,
        author_gateway: AuthorGatewayInterface,
    ) -> BookEntity:
        author = await AuthorUseCases.get_or_create_author(
            name=book_data.author.name,
            author_gateway=author_gateway,
        )

        book = BookEntity(
            id=book_data.id, title=book_data.title, author=author
        )
        new_book = await book_gateway.update_book(book)

        return new_book

    @staticmethod
    async def delete_book(
        book_id: str,
        book_gateway: BookGatewayInterface,
    ) -> None:
        await book_gateway.delete_book(book_id)
