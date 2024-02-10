from abc import ABC, abstractmethod
from typing import List

from core.domain.entities.event import Event as EventEntity


class EventGatewayInterface(ABC):
    @abstractmethod
    def create_event(self, event: EventEntity) -> EventEntity:
        raise NotImplementedError

    @abstractmethod
    def get_events(self) -> List[EventEntity]:
        raise NotImplementedError
