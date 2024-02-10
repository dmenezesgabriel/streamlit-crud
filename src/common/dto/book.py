import uuid
from typing import Union


class BookAuthorDTO:
    def __init__(self, id: Union[uuid.UUID, None], name) -> None:
        self.id = id
        self.name = name


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
