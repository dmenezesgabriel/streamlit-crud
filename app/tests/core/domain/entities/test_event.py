import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType
from src.core.domain.exceptions import InvalidEventType, InvalidModelId


@pytest.fixture
def author_mock() -> AuthorEntity:
    return AuthorEntity(name="J. R. R. Tolkien")


class TestEvent:
    @pytest.mark.parametrize(
        "event_type", [EventType.CREATED, EventType.UPDATED, EventType.DELETED]
    )
    def test_should_create_event(
        self, author_mock: AuthorEntity, event_type: EventType
    ) -> None:
        event = EventEntity(
            event_type=event_type,
            model_type="authors",
            model_id=author_mock.id,
            payload={"old": {}, "new": author_mock.to_dict()},
        )
        assert event

    @pytest.mark.parametrize(
        "event_type", [0, {}, [], True, "created", "updated", "deleted"]
    )
    def test_should_not_create_event_wrong_event_type(
        self, author_mock: AuthorEntity, event_type: EventType
    ) -> None:
        with pytest.raises(InvalidEventType):
            EventEntity(
                event_type=event_type,
                model_type="authors",
                model_id=author_mock.id,
                payload={"old": {}, "new": author_mock.to_dict()},
            )

    @pytest.mark.parametrize(
        "model_id", [0, {}, [], True, "created", "updated", "deleted"]
    )
    def test_should_not_create_event_wrong_model_id_type(
        self, author_mock: AuthorEntity, model_id: str
    ) -> None:
        with pytest.raises(InvalidModelId):
            EventEntity(
                event_type=EventType.CREATED,
                model_type="authors",
                model_id=model_id,
                payload={"old": {}, "new": author_mock.to_dict()},
            )
