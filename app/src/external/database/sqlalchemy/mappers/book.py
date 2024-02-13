from typing import cast

from src.core.domain.entities.book import Book as BookEntity
from src.external.database.sqlalchemy.mappers.author import AuthorMapper
from src.external.database.sqlalchemy.models.book import Book as BookModel


class BookMapper:
    @staticmethod
    def model_to_entity(book_model: BookModel) -> BookEntity:
        author_entity = AuthorMapper.model_to_entity(book_model.author)
        return BookEntity(
            id=cast(str, book_model.id),
            title=cast(str, book_model.title),
            author=author_entity,
        )

    @staticmethod
    def entity_to_model(book_entity: BookEntity) -> BookModel:
        author_model = AuthorMapper.entity_to_model(book_entity.author)
        return BookModel(
            id=book_entity.id,
            title=book_entity.title,
            author_id=author_model.id,
        )
