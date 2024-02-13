import uuid
from typing import Optional

from pydantic import BaseModel, ValidationError, validator


class BookAuthorDTO(BaseModel):
    id: Optional[str] = None
    name: str

    @validator("id")
    def id_must_be_uuid4_compliant(cls, v):
        if v:
            uuid.UUID(v, version=4)
            return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "J. R. R. Tolkien"},
                {"name": "J. K. Rowling"},
                {"name": "C. S. Lewis"},
            ]
        }
    }
