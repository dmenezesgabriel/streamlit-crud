from domain.entities.author import Author as AuthorEntity


class AuthorService:
    def __init__(self, author_repository, event_publisher):
        self.author_repository = author_repository
        self.event_publisher = event_publisher

    def get_author_by_name(self, name: str) -> AuthorEntity:
        return self.author_repository.get_author_by_name(name)

    def create_author(self, name: str) -> AuthorEntity:
        author = AuthorEntity(name=name)
        return self.author_repository.create_author(author)
