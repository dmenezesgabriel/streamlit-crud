from typing import Dict, List

from common.interfaces.event_gateway import EventGatewayInterface
from core.domain.entities.event import Event as EventEntity


class EventUseCase:

    @staticmethod
    def get_events(
        event_gateway: EventGatewayInterface,
    ) -> List[EventEntity]:
        return event_gateway.get_events()

    @staticmethod
    def create_event(
        id: str,
        event_type: str,
        model_type: str,
        model_id: str,
        payload: Dict[str, str],
        event_gateway: EventGatewayInterface,
    ) -> EventEntity:
        event = EventEntity(
            id=id,
            event_type=event_type,
            model_type=model_type,
            model_id=model_id,
            payload=payload,
        )
        return event_gateway.create_event(event)
