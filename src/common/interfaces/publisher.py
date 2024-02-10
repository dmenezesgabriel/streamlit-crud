from abc import ABC, abstractmethod


class BaseEventPublisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber):
        raise NotImplementedError

    @abstractmethod
    def remove_subscriber(self, subscriber):
        raise NotImplementedError

    @abstractmethod
    def publish_event(self, event):
        raise NotImplementedError
