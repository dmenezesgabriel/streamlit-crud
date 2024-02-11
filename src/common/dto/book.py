import uuid
from typing import Union

from common.dto.author import BookAuthorDTO


class NewBookDTO:
    def __init__(self, title: str, author: BookAuthorDTO) -> None:
        self.title = title
        self.author = author


class BookDTO:
    def __init__(
        self, id: uuid.UUID, title: str, author: BookAuthorDTO
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
