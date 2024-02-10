from core.utils.identifiers import generate_uuid


class Event:
    def __init__(
        self,
        id=None,
        event_type=None,
        model_type=None,
        model_id=None,
        payload=None,
    ):
        self.id = id if id else generate_uuid()
        self.event_type = event_type
        self.model_type = model_type
        self.model_id = model_id
        self.payload = payload
