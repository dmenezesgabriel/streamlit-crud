from typing import List

from sqlalchemy.future import select
from src.common.interfaces.event_repository import EventRepositoryInterface
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.exceptions import OperationalError
from src.external.database.sqlalchemy.mappers.event import EventMapper
from src.external.database.sqlalchemy.models.event import Event as EventModel
from src.external.database.sqlalchemy.session_mixing import (
    use_database_session,
)


class EventRepository(EventRepositoryInterface):
    async def create_event(self, event: EventEntity) -> EventEntity:
        async with use_database_session() as session:
            event_model = EventMapper.entity_to_model(event)
            session.add(event_model)
            await session.commit()
            result = await session.execute(
                select(EventModel).where(EventModel.id == event_model.id)
            )
            created_event = result.scalars().first()
            if not created_event:
                raise OperationalError("Could not create Event")
            return EventMapper.model_to_entity(created_event)

    async def get_events(self) -> List[EventEntity]:
        async with use_database_session() as session:
            result = await session.execute(select(EventModel))
            events = result.scalars().all()
            return [EventMapper.model_to_entity(event) for event in events]
