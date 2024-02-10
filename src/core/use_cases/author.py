from common.interfaces.author_repository import AuthorRepository
from core.domain.entities.author import Author as AuthorEntity


class AuthorUseCases:
    @staticmethod
    def get_author_by_name(
        name: str,
        author_repository: AuthorRepository,
    ) -> AuthorEntity:
        return author_repository.get_author_by_name(name)

    @staticmethod
    def create_author(
        name: str,
        author_repository: AuthorRepository,
    ) -> AuthorEntity:
        author = AuthorEntity(name=name)
        return author_repository.create_author(author)

    @staticmethod
    def get_or_create_author(
        name: str,
        author_repository: AuthorRepository,
    ) -> AuthorEntity:
        existing_author = AuthorUseCases.get_author_by_name(
            name=name,
            author_repository=author_repository,
        )

        if existing_author:
            author = existing_author
        else:
            author = AuthorUseCases.create_author(
                name=name,
                author_repository=author_repository,
            )
        return author
