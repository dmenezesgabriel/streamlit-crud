from typing import cast

from src.core.domain.entities.author import Author as AuthorEntity
from src.external.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)


class AuthorMapper:
    @staticmethod
    def model_to_entity(author_model: AuthorModel) -> AuthorEntity:
        return AuthorEntity(
            id=cast(str, author_model.id), name=cast(str, author_model.name)
        )

    @staticmethod
    def entity_to_model(author_entity: AuthorEntity) -> AuthorModel:
        return AuthorModel(id=author_entity.id, name=author_entity.name)
