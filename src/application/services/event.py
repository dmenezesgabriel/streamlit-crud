from typing import List

from domain.entities.event import Event as EventEntity


class EventService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def create_event(
        self, id, event_type, model_type, model_id, payload
    ) -> EventEntity:
        event = EventEntity(
            id=id,
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
        )
        return self.event_repository.create_event(event)

    def get_events(self) -> List[EventEntity]:
        return self.event_repository.get_events()
