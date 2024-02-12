from enum import Enum, unique
from typing import Dict, Union

from core.utils.identifiers import generate_uuid


@unique
class EventType(Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class Event:

    def __init__(
        self,
        id: Union[str, None] = None,
        *,
        event_type: EventType,
        model_type: str,
        model_id: str,
        payload: Dict[str, str],
    ) -> None:
        if not isinstance(event_type, EventType):
            raise ValueError(
                f"Invalid event_type: {event_type}. Must be a member of EventType enum."
            )

        self.id = id if id else generate_uuid()
        self.event_type = event_type
        self.model_type = model_type
        self.model_id = model_id
        self.payload = payload
