import uuid
from enum import Enum, unique
from typing import Dict, Union

from src.common.types.event import EventPayloadDictType
from src.core.domain.exceptions import InvalidEventType, InvalidModelId
from src.core.utils.identifiers import generate_uuid


@unique
class EventType(Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"

    def __str__(self) -> str:
        return self.value


class Event:

    def __init__(
        self,
        id: Union[str, None] = None,
        *,
        event_type: EventType,
        model_type: str,
        model_id: str,
        payload: EventPayloadDictType,
    ) -> None:
        if not isinstance(event_type, EventType):
            raise InvalidEventType(
                f"Invalid event_type: {event_type}. Must be a member of EventType enum."
            )

        if not self._is_valid_uuid(model_id):
            raise InvalidModelId(
                "Invalid model_id. Must be a valid UUID version 4."
            )

        self.id = id if id else generate_uuid()
        self.event_type = event_type
        self.model_type = model_type
        self.model_id = model_id
        self.payload = payload

    def _is_valid_uuid(self, uuid_string: str) -> Union[str, bool]:
        try:
            uuid_obj = uuid.UUID(uuid_string, version=4)
            return str(uuid_obj) == uuid_string
        except AttributeError:
            return False
        except ValueError:
            return False
