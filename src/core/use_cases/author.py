from common.interfaces.author_gateway import AuthorGatewayInterface
from core.domain.entities.author import Author as AuthorEntity


class AuthorUseCases:
    @staticmethod
    def get_author_by_name(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        return author_gateway.get_author_by_name(name)

    @staticmethod
    def create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        author = AuthorEntity(name=name)
        return author_gateway.create_author(author)

    @staticmethod
    def get_or_create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> AuthorEntity:
        existing_author = AuthorUseCases.get_author_by_name(
            name=name,
            author_gateway=author_gateway,
        )

        if existing_author:
            author = existing_author
        else:
            author = AuthorUseCases.create_author(
                name=name,
                author_gateway=author_gateway,
            )
        return author
