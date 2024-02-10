from typing import List

from core.domain.entities.event import Event as EventEntity
from external.database.sqlalchemy.mappers.event import EventMapper
from external.database.sqlalchemy.models.event import Event as EventModel
from external.database.sqlalchemy.session_mixing import use_database_session


class EventRepository:
    def create_event(self, event: EventEntity):
        with use_database_session() as db:
            event_model = EventMapper.entity_to_model(event)
            db.add(event_model)
            db.commit()
            db.refresh(event_model)
            return EventMapper.model_to_entity(event_model)

    def get_events(self) -> List[EventEntity]:
        with use_database_session() as db:
            events = db.query(EventModel).all()
            return [EventMapper.model_to_entity(event) for event in events]
