from typing import List

from src.common.dto.author import BookAuthorDTO
from src.common.dto.book import BookDTO, EditBookDTO, NewBookDTO
from src.common.interfaces.author_repository import AuthorRepositoryInterface
from src.common.interfaces.book_repository import BookRepositoryInterface
from src.common.interfaces.event_repository import EventRepositoryInterface
from src.communication.gateway.author import AuthorGateway
from src.communication.gateway.book import BookGateway
from src.communication.gateway.event import EventGateway
from src.core.domain.entities.book import Book as BookEntity
from src.core.use_cases.book import BookUseCases


class BookController:
    def __init__(
        self,
        book_repository: BookRepositoryInterface,
        author_repository: AuthorRepositoryInterface,
        event_repository: EventRepositoryInterface,
    ):
        self.book_repository = book_repository
        self.author_repository = author_repository
        self.event_repository = event_repository

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
        event_gateway = EventGateway(self.event_repository)

        book_author_dto = BookAuthorDTO(name=author_name)
        new_book_dto = NewBookDTO(title=title, author=book_author_dto)

        return await BookUseCases.create_book(
            new_book_data=new_book_dto,
            book_gateway=book_gateway,
            author_gateway=author_gateway,
            event_gateway=event_gateway,
        )

    async def update_book(
        self,
        book_id: str,
        title: str,
        author_name: str,
    ) -> BookEntity:
        book_gateway = BookGateway(self.book_repository)
        author_gateway = AuthorGateway(self.author_repository)
        event_gateway = EventGateway(self.event_repository)

        book_author_dto = BookAuthorDTO(name=author_name)
        book_dto = EditBookDTO(id=book_id, title=title, author=book_author_dto)

        return await BookUseCases.update_book(
            book_data=book_dto,
            book_gateway=book_gateway,
            author_gateway=author_gateway,
            event_gateway=event_gateway,
        )

    async def delete_book(self, book_id: str) -> None:
        book_gateway = BookGateway(self.book_repository)
        event_gateway = EventGateway(self.event_repository)

        await BookUseCases.delete_book(
            book_id=book_id,
            book_gateway=book_gateway,
            event_gateway=event_gateway,
        )
