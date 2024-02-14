from typing import Dict, Union

from src.common.types.author import AuthorDictType
from src.common.types.book import BookDictType
from typing_extensions import TypedDict

EventPayloadDictType = TypedDict(
    "EventPayloadDictType",
    {
        "old": Union[BookDictType, AuthorDictType, Dict[None, None]],
        "new": Union[BookDictType, AuthorDictType, Dict[None, None]],
    },
)
