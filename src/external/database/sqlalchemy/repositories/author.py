from common.interfaces.author_repository import AuthorRepositoryInterface
from core.domain.entities.author import Author as AuthorEntity
from external.database.sqlalchemy.mappers.author import AuthorMapper
from external.database.sqlalchemy.models.author import Author as AuthorModel
from external.database.sqlalchemy.session_mixing import use_database_session


class AuthorRepository(AuthorRepositoryInterface):
    def get_author_by_name(self, name: str) -> AuthorEntity:
        with use_database_session() as db:
            author = db.query(AuthorModel).filter_by(name=name).first()
            if author:
                return AuthorMapper.model_to_entity(author)
            else:
                return None

    def create_author(self, author: AuthorEntity) -> AuthorEntity:
        with use_database_session() as db:
            author_model = AuthorMapper.entity_to_model(author)
            db.add(author_model)
            db.commit()
            db.refresh(author_model)
            return AuthorMapper.model_to_entity(author_model)
