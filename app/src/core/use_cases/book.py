from typing import List, Union

from src.common.dto.book import BookDTO, EditBookDTO, NewBookDTO
from src.common.interfaces.author_gateway import AuthorGatewayInterface
from src.common.interfaces.book_gateway import BookGatewayInterface
from src.common.interfaces.event_gateway import EventGatewayInterface
from src.core.domain.entities.book import Book as BookEntity
from src.core.domain.entities.event import EventType
from src.core.domain.exceptions import BookAlreadyExists
from src.core.use_cases.author import AuthorUseCases
from src.core.use_cases.event import EventUseCase


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
    async def get_book_by_title_and_author_id(
        title: str, author_id: str, book_gateway: BookGatewayInterface
    ) -> Union[BookEntity, None]:
        return await book_gateway.get_book_by_title_and_author_id(
            title=title, author_id=author_id
        )

    @staticmethod
    async def create_book(
        new_book_data: NewBookDTO,
        book_gateway: BookGatewayInterface,
        author_gateway: AuthorGatewayInterface,
        event_gateway: EventGatewayInterface,
    ) -> BookEntity:
        author = await AuthorUseCases.get_or_create_author(
            name=new_book_data.author.name,
            author_gateway=author_gateway,
            event_gateway=event_gateway,
        )

        existing_book = await BookUseCases.get_book_by_title_and_author_id(
            title=new_book_data.title,
            author_id=author.id,
            book_gateway=book_gateway,
        )

        if existing_book:
            raise BookAlreadyExists(
                "Book with this title and author already exist"
            )

        book = BookEntity(title=new_book_data.title, author=author)

        new_book = await book_gateway.create_book(book)

        await EventUseCase.create_event(
            event_type=EventType.CREATED,
            model_type="books",
            model_id=new_book.id,
            payload={"old": {}, "new": new_book.to_dict()},
            event_gateway=event_gateway,
        )
        return new_book

    @staticmethod
    async def update_book(
        book_data: EditBookDTO,
        book_gateway: BookGatewayInterface,
        author_gateway: AuthorGatewayInterface,
        event_gateway: EventGatewayInterface,
    ) -> BookEntity:
        author = await AuthorUseCases.get_or_create_author(
            name=book_data.author.name,
            author_gateway=author_gateway,
            event_gateway=event_gateway,
        )

        old_book = await BookUseCases.get_book(
            book_id=book_data.id, book_gateway=book_gateway
        )

        book = BookEntity(
            id=book_data.id, title=book_data.title, author=author
        )
        new_book = await book_gateway.update_book(book)

        await EventUseCase.create_event(
            event_type=EventType.UPDATED,
            model_type="books",
            model_id=new_book.id,
            payload={"old": old_book.to_dict(), "new": new_book.to_dict()},
            event_gateway=event_gateway,
        )

        return new_book

    @staticmethod
    async def delete_book(
        book_id: str,
        book_gateway: BookGatewayInterface,
        event_gateway: EventGatewayInterface,
    ) -> None:
        old_book = await BookUseCases.get_book(
            book_id=book_id, book_gateway=book_gateway
        )

        await book_gateway.delete_book(book_id)

        await EventUseCase.create_event(
            event_type=EventType.DELETED,
            model_type="books",
            model_id=book_id,
            payload={"old": old_book.to_dict(), "new": {}},
            event_gateway=event_gateway,
        )

        return None
