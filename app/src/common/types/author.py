from typing import Dict, TypedDict, Union

AuthorDictType = TypedDict(
    "AuthorDictType", {"id": Union[str, None], "name": str}
)
