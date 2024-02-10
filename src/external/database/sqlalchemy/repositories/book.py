from typing import List, Union

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.exc import NoResultFound

from common.interfaces.book_repository import BookRepositoryInterface
from core.domain.entities.book import Book as BookEntity
from external.database.sqlalchemy.mappers.book import BookMapper
from external.database.sqlalchemy.models.book import Book as BookModel
from external.database.sqlalchemy.session_mixing import use_database_session


class BookRepository(BookRepositoryInterface):
    async def create_book(self, book: BookEntity) -> BookEntity:
        async with use_database_session() as session:
            async with session.begin():
                book_model = BookMapper.entity_to_model(book)
                session.add(book_model)
            created_book = await session.get(BookModel, book_model.id)
            created_book.author = await created_book.awaitable_attrs.author
            return BookMapper.model_to_entity(created_book)

    async def get_books(self) -> List[BookEntity]:
        async with use_database_session() as session:
            books = await session.scalars(
                select(BookModel).options(selectinload(BookModel.author))
            )
            return [BookMapper.model_to_entity(book) for book in books]

    async def get_book(self, book_id: int) -> BookEntity:
        async with use_database_session() as session:
            book = await session.get(BookModel, book_id)
            book.author = await book.awaitable_attrs.author
            if book:
                return BookMapper.model_to_entity(book)
            else:
                raise NoResultFound("Book not found")

    async def update_book(self, book: BookEntity) -> Union[BookEntity, None]:
        async with use_database_session() as session:
            result = await session.scalars(
                select(BookModel).filter_by(id=book.id)
            )
            book_model = result.first()
            if book_model:
                book_model.title = book.title
                book_model.author_id = book.author.id
                await session.commit()
                updated_book = await session.get(BookModel, book_model.id)
                updated_book.author = await updated_book.awaitable_attrs.author
                return BookMapper.model_to_entity(updated_book)
            else:
                raise NoResultFound("Book not found")

    async def delete_book(self, book_id: int) -> None:
        async with use_database_session() as session:
            result = await session.scalars(
                select(BookModel).filter_by(id=book_id)
            )
            book = result.first()
            if book:
                await session.delete(book)
                await session.commit()
