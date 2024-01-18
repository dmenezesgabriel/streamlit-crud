from entities import Author as AuthorEntity
from models import Author


class AuthorMapper:
    @staticmethod
    def model_to_entity(author_model):
        return AuthorEntity(id=author_model.id, name=author_model.name)

    @staticmethod
    def entity_to_model(author_entity):
        return Author(id=author_entity.id, name=author_entity.name)
