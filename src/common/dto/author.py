import uuid
from typing import Union


class BookAuthorDTO:
    def __init__(
        self, id: Union[uuid.UUID, None] = None, *, name: str
    ) -> None:
        self.id = id
        self.name = name
