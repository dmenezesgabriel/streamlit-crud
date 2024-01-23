from dataclasses import dataclass

from domain.enum.book_event_type import BookEventType


@dataclass
class BaseBookEvent:
    book_id: int
    event_type: BookEventType
