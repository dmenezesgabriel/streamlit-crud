import uuid
from typing import Dict, Union

from core.domain.entities.author import Author as AuthorEntity
from core.domain.exceptions import (
    BookAuthorNotAuthorEntityInstance,
    BookTitleNotInformed,
)
from core.utils.identifiers import generate_uuid


class Book:
    def __init__(
        self,
        id: Union[uuid.UUID, None] = None,
        *,
        title: str,
        author: AuthorEntity,
    ) -> None:
        if title is None or len(title) == 0:
            raise BookTitleNotInformed("Book title should be informed")

        if not isinstance(author, AuthorEntity):
            raise BookAuthorNotAuthorEntityInstance(
                "Book's Author not Author entity type"
            )

        self.id = id if id else generate_uuid()
        self.title = title
        self.author = author
