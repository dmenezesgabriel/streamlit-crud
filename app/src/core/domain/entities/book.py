import json
from typing import Union

from src.common.types.book import BookDictType
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.exceptions import (
    BookAuthorNotAuthorEntityInstance,
    BookTitleNotInformed,
)
from src.core.utils.identifiers import generate_uuid


class Book:
    def __init__(
        self,
        id: Union[str, None] = None,
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

    def to_dict(self) -> BookDictType:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.to_dict(),
        }
