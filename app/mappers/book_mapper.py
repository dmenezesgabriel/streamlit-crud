from entities import Book as BookEntity
from mappers.author_mapper import AuthorMapper
from models.book import Book as BookModel


class BookMapper:
    @staticmethod
    def model_to_entity(book_model):
        author_entity = AuthorMapper.model_to_entity(book_model.author)
        return BookEntity(
            id=book_model.id, title=book_model.title, author=author_entity
        )

    @staticmethod
    def entity_to_model(book_entity):
        author_model = AuthorMapper.entity_to_model(book_entity.author)
        return BookModel(
            id=book_entity.id, title=book_entity.title, author=author_model
        )
