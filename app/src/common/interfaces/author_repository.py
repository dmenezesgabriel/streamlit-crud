from abc import ABC, abstractmethod
from typing import Union

from src.core.domain.entities.author import Author as AuthorEntity


class AuthorRepositoryInterface(ABC):
    @abstractmethod
    async def get_author_by_name(self, name: str) -> Union[AuthorEntity, None]:
        raise NotImplementedError

    @abstractmethod
    async def create_author(self, author: AuthorEntity) -> AuthorEntity:
        raise NotImplementedError
