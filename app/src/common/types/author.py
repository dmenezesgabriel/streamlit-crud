from typing import Union

from typing_extensions import TypedDict

AuthorDictType = TypedDict(
    "AuthorDictType", {"id": Union[str, None], "name": str}
)
