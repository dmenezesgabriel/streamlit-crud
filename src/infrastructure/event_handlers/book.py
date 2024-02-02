import logging

from application.event_handlers.base_handler import BaseEventHandler
from domain.events.base_book_event import BaseBookEvent
from utils.identifiers import generate_uuid

logger = logging.getLogger("app")


class BookEventHandler(BaseEventHandler):
    def __init__(self, event_service):
        self.id = generate_uuid()
        self.event_service = event_service

    def handle_event(self, event: BaseBookEvent):
        if not isinstance(event, BaseBookEvent):
            logger.info("Not a book event")
        else:
            logger.info(event)
