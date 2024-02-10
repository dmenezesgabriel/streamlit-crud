from abc import ABC, abstractmethod


class BaseEventHandler(ABC):
    @abstractmethod
    def handle_event(self, event):
        pass
