from dataclasses import dataclass

from domain.enum.book_event_type import BookEventType
from domain.events.base_book_event import BaseBookEvent


@dataclass
class BookCreatedEvent(BaseBookEvent):
    def __init__(self, book_id: str, title: str, author: str):
        super().__init__(
            book_id=book_id,
            event_type=BookEventType.CREATED,
        )
        self.title = title
        self.author = author
