from typing import Union

from src.common.interfaces.author_gateway import AuthorGatewayInterface
from src.common.interfaces.author_repository import AuthorRepositoryInterface
from src.core.domain.entities.author import Author as AuthorEntity


class AuthorGateway(AuthorGatewayInterface):
    def __init__(self, author_repository: AuthorRepositoryInterface):
        self.author_repository = author_repository

    async def get_author_by_name(self, name: str) -> Union[AuthorEntity, None]:
        author: Union[AuthorEntity, None] = (
            await self.author_repository.get_author_by_name(name=name)
        )
        return author

    async def create_author(self, author: AuthorEntity) -> AuthorEntity:
        author: AuthorEntity = await self.author_repository.create_author(
            author=author
        )
        return author
