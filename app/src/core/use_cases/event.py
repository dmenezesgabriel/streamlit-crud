from typing import Dict, List, Union

from src.common.interfaces.event_gateway import EventGatewayInterface
from src.common.types.event import EventPayloadDictType
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType


class EventUseCase:

    @staticmethod
    async def get_events(
        event_gateway: EventGatewayInterface,
    ) -> List[EventEntity]:
        return await event_gateway.get_events()

    @staticmethod
    async def create_event(
        event_type: EventType,
        model_type: str,
        model_id: str,
        payload: EventPayloadDictType,
        event_gateway: EventGatewayInterface,
    ) -> EventEntity:
        event = EventEntity(
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
        )
        return await event_gateway.create_event(event)
