from typing import Dict, TypedDict, Union

from src.common.types.author import authorDictType

bookDictType = TypedDict(
    "bookDictType",
    {
        "id": Union[str, None],
        "title": "str",
        "author": authorDictType,
    },
)
