from domain.entities.author import Author as AuthorEntity
from infrastructure.database.sqlalchemy.repositories.books import (
    AuthorRepository,
)


class AuthorService:
    def __init__(self):
        self.author_repository = AuthorRepository()

    def get_author_by_name(self, name: str) -> AuthorEntity:
        return self.author_repository.get_author_by_name(name)

    def create_author(self, name: str) -> AuthorEntity:
        return self.author_repository.create_author(name)
