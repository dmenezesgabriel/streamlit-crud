from core.domain.entities.book import Book as BookEntity
from external.database.sqlalchemy.mappers.author import AuthorMapper
from external.database.sqlalchemy.models.book import Book as BookModel


class BookMapper:
    @staticmethod
    def model_to_entity(book_model: BookModel) -> BookEntity:
        author_entity = AuthorMapper.model_to_entity(book_model.author)
        return BookEntity(
            id=book_model.id, title=book_model.title, author=author_entity
        )

    @staticmethod
    def entity_to_model(book_entity: BookEntity) -> BookModel:
        author_model = AuthorMapper.entity_to_model(book_entity.author)
        return BookModel(
            id=book_entity.id,
            title=book_entity.title,
            author_id=author_model.id,
        )
