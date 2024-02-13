from unittest.mock import MagicMock

import pytest

from communication.gateway.event import EventGateway
from core.domain.entities.author import Author as AuthorEntity
from core.domain.entities.event import Event, EventType
from core.use_cases.event import EventUseCase
from core.utils.identifiers import generate_uuid


@pytest.fixture
def author():
    return AuthorEntity(name="J. R. R. Tolkien")


class TestEventUseCase:
    @pytest.fixture
    def event_gateway_mock(self):
        return MagicMock(spec=EventGateway)

    @pytest.mark.asyncio
    async def test_get_events_call_gateway_event_get_events_once(
        self, author, event_gateway_mock
    ):
        _id = generate_uuid()

        event_gateway_mock.get_events.return_value = [
            Event(
                id=_id,
                event_type=EventType.CREATED,
                model_type="authors",
                model_id=author.id,
                payload={},
            )
        ]

        # Call the method under test
        events = await EventUseCase.get_events(event_gateway_mock)

        # Assert the call count
        event_gateway_mock.get_events.assert_called_once()

        # Additional assertions based on the mocked return value
        assert len(events) == 1
        assert events[0].id == _id
        assert events[0].event_type == EventType.CREATED
        assert events[0].model_type == "authors"
        assert events[0].model_id == author.id
        assert events[0].payload == {}
