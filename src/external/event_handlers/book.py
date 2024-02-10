import logging

from common.interfaces.event_handler import BaseEventHandler
from core.domain.events.base_book_event import BaseBookEvent
from core.utils.identifiers import generate_uuid

logger = logging.getLogger("app")


class BookEventHandler(BaseEventHandler):
    def __init__(self):
        self.id = generate_uuid()

    def handle_event(self, event: BaseBookEvent):
        if not isinstance(event, BaseBookEvent):
            logger.info("Not a book event")
        else:
            logger.info(event)
