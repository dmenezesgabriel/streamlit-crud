from typing import List, Union

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from src.common.interfaces.book_repository import BookRepositoryInterface
from src.core.domain.entities.book import Book as BookEntity
from src.core.domain.exceptions import BookNotFound, OperationalError
from src.external.database.sqlalchemy.mappers.book import BookMapper
from src.external.database.sqlalchemy.models.book import Book as BookModel
from src.external.database.sqlalchemy.session_mixing import (
    use_database_session,
)


class BookRepository(BookRepositoryInterface):
    async def create_book(self, book: BookEntity) -> BookEntity:
        async with use_database_session() as session:
            book_model = BookMapper.entity_to_model(book)
            session.add(book_model)
            await session.commit()
            result = await session.execute(
                select(BookModel).where(BookModel.id == book_model.id)
            )
            created_book = result.scalars().first()
            if not created_book:
                raise OperationalError("Could not create a book")
            created_book.author = await created_book.awaitable_attrs.author
            return BookMapper.model_to_entity(created_book)

    async def get_books(self) -> List[BookEntity]:
        async with use_database_session() as session:
            result = await session.execute(
                select(BookModel).options(selectinload(BookModel.author))
            )
            books = result.scalars().all()
            return [BookMapper.model_to_entity(book) for book in books]

    async def get_book(self, book_id: str) -> BookEntity:
        async with use_database_session() as session:
            result = await session.execute(
                select(BookModel).where(BookModel.id == book_id)
            )
            book = result.scalars().first()
            if book:
                book.author = await book.awaitable_attrs.author
                return BookMapper.model_to_entity(book)
            else:
                raise BookNotFound("Book not found")

    async def get_book_by_title_and_author_id(
        self, title: str, author_id: str
    ) -> Union[BookEntity, None]:
        async with use_database_session() as session:
            result = await session.execute(
                select(BookModel).where(
                    BookModel.title == title, BookModel.author_id == author_id
                )
            )
            book_model = result.scalars().first()
            if book_model:
                book_model.author = await book_model.awaitable_attrs.author
                return BookMapper.model_to_entity(book_model)
            return None

    async def update_book(self, book: BookEntity) -> Union[BookEntity, None]:
        async with use_database_session() as session:
            result = await session.execute(
                select(BookModel).where(BookModel.id == book.id)
            )
            book_model = result.scalars().first()
            if book_model:
                await session.execute(
                    update(BookModel)
                    .where(BookModel.id == book.id)
                    .values(title=book.title, author_id=book.author.id)
                )
                await session.commit()

                updated_book_query = await session.execute(
                    select(BookModel).where(BookModel.id == book_model.id)
                )
                updated_book = updated_book_query.scalars().first()

                if not updated_book:
                    raise BookNotFound("Book not found")

                updated_book.author = await updated_book.awaitable_attrs.author
                return BookMapper.model_to_entity(updated_book)
            else:
                raise BookNotFound("Book not found")

    async def delete_book(self, book_id: str) -> None:
        async with use_database_session() as session:
            result = await session.execute(
                select(BookModel).where(BookModel.id == book_id)
            )
            book = result.scalars().first()
            if book:
                await session.delete(book)
                await session.commit()
