from dataclasses import dataclass

from domain.enum.book_event_type import BookEventType
from domain.events.base_book_event import BaseBookEvent


@dataclass
class BookDeletedEvent(BaseBookEvent):
    def __init__(self, book_id: str):
        super().__init__(
            book_id=book_id,
            event_type=BookEventType.DELETED,
        )
