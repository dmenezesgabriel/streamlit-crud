from typing import Dict, TypedDict, Union

from src.common.types.author import AuthorDictType

BookDictType = TypedDict(
    "BookDictType",
    {
        "id": Union[str, None],
        "title": "str",
        "author": AuthorDictType,
    },
)
