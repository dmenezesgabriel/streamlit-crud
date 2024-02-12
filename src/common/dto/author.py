import uuid
from typing import Optional

from pydantic import BaseModel


class BookAuthorDTO(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "J. R. R. Tolkien"},
                {"name": "J. K. Rowling"},
                {"name": "C. S. Lewis"},
            ]
        }
    }
