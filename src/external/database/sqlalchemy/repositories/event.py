from typing import List

from sqlalchemy.future import select

from common.interfaces.event_repository import EventRepositoryInterface
from core.domain.entities.event import Event as EventEntity
from external.database.sqlalchemy.mappers.event import EventMapper
from external.database.sqlalchemy.models.event import Event as EventModel
from external.database.sqlalchemy.session_mixing import use_database_session


class EventRepository(EventRepositoryInterface):
    async def create_event(self, event: EventEntity) -> EventEntity:
        async with use_database_session() as session:
            async with session.begin():
                event_model = EventMapper.entity_to_model(event)
                session.add(event_model)
            created_event = await session.get(EventModel, event_model.id)
            return EventMapper.model_to_entity(created_event)

    async def get_events(self) -> List[EventEntity]:
        async with use_database_session() as session:
            events = await session.execute(select(EventModel))
            return [EventMapper.model_to_entity(event) for event in events]
