from abc import ABC, abstractmethod
from typing import List

from src.core.domain.entities.event import Event as EventEntity


class EventRepositoryInterface(ABC):
    @abstractmethod
    async def create_event(self, event: EventEntity) -> EventEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_events(self) -> List[EventEntity]:
        raise NotImplementedError
