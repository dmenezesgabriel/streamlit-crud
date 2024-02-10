from abc import ABC, abstractmethod

from core.domain.entities.author import Author as AuthorEntity


class AuthorRepository(ABC):
    @abstractmethod
    def get_author_by_name(self, name: str) -> AuthorEntity:
        raise NotImplementedError

    @abstractmethod
    def create_author(self, author) -> AuthorEntity:
        raise NotImplementedError
