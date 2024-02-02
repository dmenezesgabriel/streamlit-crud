from application.interfaces.publisher import BaseEventPublisher


class EventPublisher(BaseEventPublisher):
    def __init__(self):
        self.subscribers = {}

    def add_subscriber(self, subscriber):
        key = subscriber.id
        if key not in self.subscribers:
            self.subscribers[key] = subscriber

    def remove_subscriber(self, subscriber):
        key = subscriber.id
        if key in self.subscribers:
            del self.subscribers[key]

    def publish_event(self, event):
        for subscriber in self.subscribers.values():
            subscriber.handle_event(event)
