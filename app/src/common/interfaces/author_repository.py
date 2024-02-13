from abc import ABC, abstractmethod
from typing import Union

from src.core.domain.entities.author import Author as AuthorEntity


class AuthorRepositoryInterface(ABC):
    @abstractmethod
    def get_author_by_name(self, name: str) -> Union[AuthorEntity, None]:
        raise NotImplementedError

    @abstractmethod
    def create_author(self, author: AuthorEntity) -> AuthorEntity:
        raise NotImplementedError
