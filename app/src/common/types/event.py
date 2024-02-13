from typing import Dict, TypedDict, Union

from src.common.types.author import AuthorDictType
from src.common.types.book import BookDictType

EventPayloadDictType = TypedDict(
    "EventPayloadDictType",
    {
        "old": Union[BookDictType, AuthorDictType, Dict[None, None]],
        "new": Union[BookDictType, AuthorDictType, Dict[None, None]],
    },
)
