from typing import List

from application.interfaces.event_repository import EventRepository
from domain.entities.event import Event as EventEntity


class EventUseCase:

    @staticmethod
    def get_events(event_repository: EventRepository) -> List[EventEntity]:
        return event_repository.get_events()

    @staticmethod
    def create_event(
        id: str,
        event_type: str,
        model_type: str,
        model_id: str,
        payload: dict,
        event_repository: EventRepository,
    ) -> EventEntity:
        event = EventEntity(
            id=id,
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
        )
        return event_repository.create_event(event)
