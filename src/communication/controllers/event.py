from typing import Dict, List

from communication.gateway.event import EventGateway
from core.domain.entities.event import Event as EventEntity
from core.use_cases.event import EventUseCase


class EventController:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def get_events(self) -> List[EventEntity]:
        event_gateway = EventGateway(self.event_repository)
        return await EventUseCase.get_events(event_gateway=event_gateway)

    async def create_event(
        self,
        id: str,
        event_type: str,
        model_type: str,
        model_id: str,
        payload: Dict[str, str],
    ) -> EventEntity:
        event_gateway = EventGateway(self.event_repository)
        return await EventUseCase.create_event(
            id=id,
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
            event_gateway=event_gateway,
        )
