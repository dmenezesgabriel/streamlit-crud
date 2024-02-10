from enum import Enum


class BookEventType(Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"
