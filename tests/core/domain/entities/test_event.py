from uuid import UUID

import pytest

from core.domain.entities.author import Author as AuthorEntity
from core.domain.entities.event import Event as EventEntity
from core.domain.entities.event import EventType
from core.domain.exceptions import InvalidEventType, InvalidModelId


@pytest.fixture
def author():
    return AuthorEntity(name="J. R. R. Tolkien")


class TestEvent:
    @pytest.mark.parametrize(
        "event_type", [EventType.CREATED, EventType.UPDATED, EventType.DELETED]
    )
    def test_create_event(self, author, event_type):
        event = EventEntity(
            event_type=event_type,
            model_type="authors",
            model_id=author.id,
            payload={"old": {}, "new": author.to_dict()},
        )
        assert event

    @pytest.mark.parametrize(
        "event_type", [0, {}, [], True, "created", "updated", "deleted"]
    )
    def test_create_event_wrong_event_type(self, author, event_type):
        with pytest.raises(InvalidEventType):
            EventEntity(
                event_type=event_type,
                model_type="authors",
                model_id=author.id,
                payload={"old": {}, "new": author.to_dict()},
            )

    @pytest.mark.parametrize(
        "model_id", [0, {}, [], True, "created", "updated", "deleted"]
    )
    def test_create_event_wrong_model_id_type(self, author, model_id):
        with pytest.raises(InvalidModelId):
            EventEntity(
                event_type=EventType.CREATED,
                model_type="authors",
                model_id=model_id,
                payload={"old": {}, "new": author.to_dict()},
            )
