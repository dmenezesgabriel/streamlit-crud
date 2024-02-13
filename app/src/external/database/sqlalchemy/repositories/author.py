from sqlalchemy.future import select

from src.external.database.sqlalchemy.mappers.author import AuthorMapper
from src.external.database.sqlalchemy.models.author import Author as AuthorModel
from src.external.database.sqlalchemy.session_mixing import use_database_session
from src.common.interfaces.author_repository import AuthorRepositoryInterface
from src.core.domain.entities.author import Author as AuthorEntity


class AuthorRepository(AuthorRepositoryInterface):
    async def get_author_by_name(self, name: str) -> AuthorEntity:
        async with use_database_session() as session:
            result = await session.scalars(
                select(AuthorModel).filter_by(name=name)
            )
            author = result.first()
            if author:
                return AuthorMapper.model_to_entity(author)
            else:
                return None

    async def create_author(self, author: AuthorEntity) -> AuthorEntity:
        async with use_database_session() as session:
            async with session.begin():
                author_model = AuthorMapper.entity_to_model(author)
                session.add(author_model)
                return AuthorMapper.model_to_entity(author_model)
