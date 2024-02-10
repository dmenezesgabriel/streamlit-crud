from common.interfaces.author_gateway import AuthorGatewayInterface
from core.domain.entities.author import Author as AuthorEntity


class AuthorUseCases:
    @staticmethod
    async def get_author_by_name(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        return await author_gateway.get_author_by_name(name)

    @staticmethod
    async def create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        author = AuthorEntity(name=name)
        return await author_gateway.create_author(author)

    @staticmethod
    async def get_or_create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        existing_author = await AuthorUseCases.get_author_by_name(
            name=name,
            author_gateway=author_gateway,
        )

        if existing_author:
            author = existing_author
        else:
            author = await AuthorUseCases.create_author(
                name=name,
                author_gateway=author_gateway,
            )
        return author
