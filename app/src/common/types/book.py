from typing import Union

from src.common.types.author import AuthorDictType
from typing_extensions import TypedDict

BookDictType = TypedDict(
    "BookDictType",
    {
        "id": Union[str, None],
        "title": "str",
        "author": AuthorDictType,
    },
)
