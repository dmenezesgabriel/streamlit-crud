import uuid
from typing import Any, List, TypedDict
from unittest.mock import MagicMock

import pytest
from src.common.interfaces.event_gateway import EventGatewayInterface
from src.common.types.event import EventPayloadDictType
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType
from src.core.domain.exceptions import InvalidEventType, InvalidModelId
from src.core.use_cases.event import EventUseCase

EventAttributes = TypedDict(
    "EventAttributes",
    {
        "event_type": EventType,
        "model_type": str,
        "model_id": str,
        "payload": EventPayloadDictType,
        "event_gateway": EventGatewayInterface,
    },
)


class TestEventUseCaseGetEvents:

    @pytest.mark.asyncio
    async def test_should_call_gateway_event_get_events_once(
        self,
        event_gateway_mock: MagicMock,
        event_list_mock: List[EventEntity],
    ) -> None:

        event_gateway_mock.get_events.return_value = event_list_mock
        await EventUseCase.get_events(event_gateway_mock)
        event_gateway_mock.get_events.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_return_events_list(
        self,
        author_mock: AuthorEntity,
        event_gateway_mock: MagicMock,
        event_mock: EventEntity,
        event_list_mock: List[EventEntity],
    ) -> None:

        event_gateway_mock.get_events.return_value = event_list_mock

        events = await EventUseCase.get_events(event_gateway_mock)

        assert isinstance(events, list)
        assert len(events) == 1
        assert isinstance(events[0], EventEntity)
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
        await EventUseCase.create_event(
            event_type=event_mock.event_type,
            model_type=event_mock.model_type,
            model_id=event_mock.model_id,
            payload=event_mock.payload,
            event_gateway=event_gateway_mock,
        )
        event_gateway_mock.create_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_return_event(
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

        assert isinstance(event, EventEntity)
        assert event.event_type == event_mock.event_type
        assert event.model_type == event_mock.model_type
        assert event.model_id == event_mock.model_id
        assert event.payload == event_mock.payload

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "attributes, exceptions",
        [
            (
                {
                    "event_type": 1,
                    "model_type": 1,
                    "model_id": 1,
                    "payload": 1,
                    "event_gateway": 1,
                },
                InvalidEventType,
            ),
            (
                {
                    "event_type": EventType.CREATED,
                    "model_type": 1,
                    "model_id": 1,
                    "payload": 1,
                    "event_gateway": 1,
                },
                InvalidModelId,
            ),
        ],
    )
    async def test_create_event_with_wrong_attributes_should_fail(
        self,
        event_gateway_mock: MagicMock,
        event_mock: EventEntity,
        attributes: EventAttributes,
        exceptions: Any,
    ) -> None:

        event_gateway_mock.create_event.return_value = event_mock
        with pytest.raises(exceptions):
            await EventUseCase.create_event(
                event_type=attributes["event_type"],
                model_type=attributes["model_type"],
                model_id=attributes["model_id"],
                payload=attributes["payload"],
                event_gateway=attributes["event_gateway"],
            )
