from typing import List

from common.interfaces.event_gateway import EventGatewayInterface
from common.interfaces.event_repository import EventRepositoryInterface
from core.domain.entities.event import Event as EventEntity
from external.database.sqlalchemy.mappers.event import EventMapper
from external.database.sqlalchemy.models.event import Event as EventModel
from external.database.sqlalchemy.session_mixing import use_database_session


class EventGateway(EventGatewayInterface):
    def __init__(self, event_repository: EventRepositoryInterface):
        self.event_repository = event_repository

    def create_event(self, event: EventEntity) -> EventEntity:
        return self.event_repository.create_event(event=event)

    def get_events(self) -> List[EventEntity]:
        return self.event_repository.get_events()
