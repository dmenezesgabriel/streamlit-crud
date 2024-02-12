import json
from typing import Dict, Union

from core.domain.exceptions import AuthorNameNotInformed
from core.utils.identifiers import generate_uuid


class Author:
    def __init__(
        self,
        id: Union[str, None] = None,
        *,
        name: str,
    ) -> None:
        if name is None or len(name) == 0:
            raise AuthorNameNotInformed("Author name should be informed")

        self.id = id if id else generate_uuid()
        self.name = name

    def to_json(self) -> Dict[str, str]:
        return {"id": self.id, "name": self.name}
