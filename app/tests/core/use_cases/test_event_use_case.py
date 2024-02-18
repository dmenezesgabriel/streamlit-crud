import uuid
from typing import List
from unittest.mock import MagicMock

import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.use_cases.event import EventUseCase


class TestEventUseCaseGetEvents:

    @pytest.mark.asyncio
    async def test_should_call_gateway_event_get_events_once(
        self,
        author_mock: AuthorEntity,
        event_gateway_mock: MagicMock,
        event_mock: EventEntity,
        event_list_mock: List[EventEntity],
    ) -> None:

        event_gateway_mock.get_events.return_value = event_list_mock

        events = await EventUseCase.get_events(event_gateway_mock)

        event_gateway_mock.get_events.assert_called_once()

        assert len(events) == 1
        assert uuid.UUID(events[0].id, version=4)
        assert events[0].event_type == event_mock.event_type
        assert events[0].model_type == event_mock.model_type
        assert events[0].model_id == author_mock.id
        assert events[0].payload == event_mock.payload


class TestEventUseCaseCreateEvent:

    @pytest.mark.asyncio
    async def test_should_call_gateway_event_create_event_once(
        self,
        event_gateway_mock: MagicMock,
        event_mock: EventEntity,
    ) -> None:

        event_gateway_mock.create_event.return_value = event_mock

        event = await EventUseCase.create_event(
            event_type=event_mock.event_type,
            model_type=event_mock.model_type,
            model_id=event_mock.model_id,
            payload=event_mock.payload,
            event_gateway=event_gateway_mock,
        )

        event_gateway_mock.create_event.assert_called_once()

        assert event.event_type == event_mock.event_type
        assert event.model_type == event_mock.model_type
        assert event.model_id == event_mock.model_id
        assert event.payload == event_mock.payload
