from typing import Dict, Union

from core.utils.identifiers import generate_uuid


class Event:

    def __init__(
        self,
        id: Union[str, None] = None,
        *,
        event_type: str,
        model_type: str,
        model_id: str,
        payload: Dict[str, str],
    ) -> None:
        self.id = id if id else generate_uuid()
        self.event_type = event_type
        self.model_type = model_type
        self.model_id = model_id
        self.payload = payload
