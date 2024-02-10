import uuid
from typing import Dict, Union

from core.utils.identifiers import generate_uuid


class Book:
    def __init__(
        self,
        id: Union[uuid.UUID, None] = None,
        *,
        title: str,
        author: str,
    ) -> None:
        self.id = id if id else generate_uuid()
        self.title = title
        self.author = author
