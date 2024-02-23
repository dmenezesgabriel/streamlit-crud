from typing import List

from src.common.interfaces.event_gateway import EventGatewayInterface
from src.common.interfaces.event_repository import EventRepositoryInterface
from src.core.domain.entities.event import Event as EventEntity


class EventGateway(EventGatewayInterface):
    def __init__(self, event_repository: EventRepositoryInterface):
        self.event_repository = event_repository

    async def create_event(self, event: EventEntity) -> EventEntity:
        return await self.event_repository.create_event(event=event)

    async def get_events(self) -> List[EventEntity]:
        return await self.event_repository.get_events()
