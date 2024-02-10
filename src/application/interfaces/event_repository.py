from abc import ABC, abstractmethod
from typing import List

from domain.entities.event import Event as EventEntity


class EventRepository(ABC):
    @abstractmethod
    def create_event(self, event: EventEntity):
        raise NotImplementedError

    @abstractmethod
    def get_events(self) -> List[EventEntity]:
        raise NotImplementedError
