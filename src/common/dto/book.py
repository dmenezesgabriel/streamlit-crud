import uuid

from pydantic import BaseModel

from common.dto.author import BookAuthorDTO
from core.utils.identifiers import generate_uuid


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
    id: uuid.UUID
    title: str
    author: BookAuthorDTO

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
