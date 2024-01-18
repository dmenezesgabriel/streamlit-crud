from entities.author import Author as AuthorEntity
from repositories.books import AuthorRepository
from sqlalchemy.orm import Session


class AuthorService:
    def __init__(self, db: Session):
        self.author_repo = AuthorRepository(db)

    def get_author_by_name(self, name: str) -> AuthorEntity:
        return self.author_repo.get_author_by_name(name)

    def create_author(self, name: str) -> AuthorEntity:
        return self.author_repo.create_author(name)
