import uuid
from typing import Union

from pydantic import BaseModel, ValidationError, validator


class BookAuthorDTO(BaseModel):
    id: Union[str, None] = None
    name: str

    @validator("id")
    def id_must_be_uuid4_compliant(cls, v: str) -> Union[str, None]:
        if v:
            uuid.UUID(v, version=4)
            return v
        return None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "J. R. R. Tolkien"},
                {"name": "J. K. Rowling"},
                {"name": "C. S. Lewis"},
            ]
        }
    }
