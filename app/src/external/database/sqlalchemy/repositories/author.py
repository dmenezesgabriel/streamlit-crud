from typing import Union

from sqlalchemy.future import select
from src.common.interfaces.author_repository import AuthorRepositoryInterface
from src.core.domain.entities.author import Author as AuthorEntity
from src.external.database.sqlalchemy.mappers.author import AuthorMapper
from src.external.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)
from src.external.database.sqlalchemy.session_mixing import (
    use_database_session,
)


class AuthorRepository(AuthorRepositoryInterface):
    async def get_author_by_name(self, name: str) -> Union[AuthorEntity, None]:
        async with use_database_session() as session:
            result = await session.execute(
                select(AuthorModel).filter_by(name=name)
            )
            author = result.scalars().first()
            if author:
                return AuthorMapper.model_to_entity(author)
            else:
                return None

    async def create_author(self, author: AuthorEntity) -> AuthorEntity:
        async with use_database_session() as session:
            author_model = AuthorMapper.entity_to_model(author)
            session.add(author_model)
            await session.commit()
            return AuthorMapper.model_to_entity(author_model)
