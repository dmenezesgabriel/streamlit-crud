from typing import cast

from src.common.types.event import EventPayloadDictType
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType
from src.external.database.sqlalchemy.models.event import Event as EventModel


class EventMapper:
    @staticmethod
    def model_to_entity(event_model: EventModel) -> EventEntity:
        return EventEntity(
            id=cast(str, event_model.id),
            event_type=EventType(cast(str, event_model.event_type)),
            model_type=cast(str, event_model.model_type),
            model_id=cast(str, event_model.model_id),
            payload=cast(EventPayloadDictType, event_model.payload),
        )

    @staticmethod
    def entity_to_model(event_entity: EventEntity) -> EventModel:
        return EventModel(
            id=event_entity.id,
            event_type=str(event_entity.event_type),
            model_type=event_entity.model_type,
            model_id=event_entity.model_id,
            payload=event_entity.payload,
        )
