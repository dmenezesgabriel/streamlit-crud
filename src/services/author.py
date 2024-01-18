from sqlalchemy.orm import Session

from domain.entities.author import Author as AuthorEntity
from infrastructure.database.sqlalchemy.repositories.books import (
    AuthorRepository,
)


class AuthorService:
    def __init__(self, db: Session):
        self.author_repo = AuthorRepository(db)

    def get_author_by_name(self, name: str) -> AuthorEntity:
        return self.author_repo.get_author_by_name(name)

    def create_author(self, name: str) -> AuthorEntity:
        return self.author_repo.create_author(name)
