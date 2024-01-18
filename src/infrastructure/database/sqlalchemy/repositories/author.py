from sqlalchemy.orm import Session

from domain.entities.author import Author as AuthorEntity
from infrastructure.database.sqlalchemy.mappers.author import AuthorMapper
from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)


class AuthorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_author_by_name(self, name: str) -> AuthorEntity:
        author = self.db.query(AuthorModel).filter_by(name=name).first()
        if author:
            return AuthorMapper.model_to_entity(author)
        else:
            return None

    def create_author(self, name: str) -> AuthorEntity:
        try:
            author = AuthorModel(name=name)
            self.db.add(author)
            self.db.commit()
            self.db.refresh(author)
            return AuthorMapper.model_to_entity(author)
        except Exception as error:
            self.db.rollback()
            raise error
