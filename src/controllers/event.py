from typing import List

from application.use_cases.event import EventUseCase
from domain.entities.event import Event as EventEntity
from infrastructure.database.sqlalchemy.repositories.event import (
    EventRepository,
)


class EventController:

    @staticmethod
    def get_events() -> List[EventEntity]:
        event_repository = EventRepository()
        return EventUseCase.get_events(event_repository=event_repository)

    @staticmethod
    def create_event(
        id: str,
        event_type: str,
        model_type: str,
        model_id: str,
        payload: dict,
    ) -> EventEntity:
        event_repository = EventRepository()
        return EventUseCase.create_event(
            id=id,
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
            event_repository=event_repository,
        )
