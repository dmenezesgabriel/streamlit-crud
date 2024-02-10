import uuid
from typing import Dict, Union

from core.utils.identifiers import generate_uuid


class Author:

    def __init__(
        self,
        id: Union[uuid.UUID, None] = None,
        *,
        name: str,
    ) -> None:
        self.id = id if id else generate_uuid()
        self.name = name
