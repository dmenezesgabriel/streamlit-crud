import uuid
from typing import Union

from pydantic import BaseModel, ValidationError, validator

from src.common.dto.author import BookAuthorDTO
from src.core.utils.identifiers import generate_uuid


class NewBookDTO(BaseModel):
    title: str
    author: BookAuthorDTO

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "The Fellowship of the Ring",
                    "author": {
                        "name": "J. R. R. Tolkien",
                    },
                },
                {
                    "title": "Harry Potter and the Philosopher's Stone",
                    "author": {
                        "name": "J. K. Rowling",
                    },
                },
                {
                    "title": "The Pilgrim's Regress",
                    "author": {
                        "name": "C. S. Lewis",
                    },
                },
            ]
        }
    }


class BookDTO(BaseModel):
    id: str
    title: str
    author: BookAuthorDTO

    @validator("id")
    def id_must_be_uuid4_compliant(cls, v: str) -> Union[str, None]:
        uuid.UUID(v, version=4)
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": generate_uuid(),
                    "title": "The Fellowship of the Ring",
                    "author": {
                        "id": generate_uuid(),
                        "name": "J. R. R. Tolkien",
                    },
                },
                {
                    "id": generate_uuid(),
                    "title": "Harry Potter and the Philosopher's Stone",
                    "author": {
                        "id": generate_uuid(),
                        "name": "J. K. Rowling",
                    },
                },
                {
                    "id": generate_uuid(),
                    "title": "The Pilgrim's Regress",
                    "author": {
                        "id": generate_uuid(),
                        "name": "C. S. Lewis",
                    },
                },
            ]
        }
    }


class EditBookDTO(BaseModel):
    id: str
    title: str
    author: BookAuthorDTO

    @validator("id")
    def id_must_be_uuid4_compliant(cls, v: str) -> Union[str, None]:
        uuid.UUID(v, version=4)
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": generate_uuid(),
                    "title": "The Fellowship of the Ring",
                    "author": {
                        "name": "J. R. R. Tolkien",
                    },
                },
                {
                    "id": generate_uuid(),
                    "title": "Harry Potter and the Philosopher's Stone",
                    "author": {
                        "name": "J. K. Rowling",
                    },
                },
                {
                    "id": generate_uuid(),
                    "title": "The Pilgrim's Regress",
                    "author": {
                        "name": "C. S. Lewis",
                    },
                },
            ]
        }
    }
