import asyncio
from typing import List
from unittest.mock import MagicMock

import pytest
from src.communication.gateway.event import EventGateway
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType


@pytest.fixture
def author_mock() -> AuthorEntity:
    return AuthorEntity(name="J. R. R. Tolkien")


@pytest.fixture
def event_mock(author_mock) -> EventEntity:
    return EventEntity(
        event_type=EventType.CREATED,
        model_type="authors",
        model_id=author_mock.id,
        payload={"old": {}, "new": author_mock.to_dict()},
    )


@pytest.fixture
def event_list_mock(author_mock) -> List[EventEntity]:
    return [
        EventEntity(
            event_type=EventType.CREATED,
            model_type="authors",
            model_id=author_mock.id,
            payload={"old": {}, "new": author_mock.to_dict()},
        )
    ]


@pytest.fixture
def author_gateway_mock() -> MagicMock:
    return MagicMock()


@pytest.fixture
def event_gateway_mock() -> MagicMock:
    return MagicMock(spec=EventGateway)


@pytest.fixture
def return_author_future(author_mock):
    future = asyncio.Future()
    future.set_result(author_mock)
    return future


@pytest.fixture
def return_event_future(event_mock):
    future = asyncio.Future()
    future.set_result(event_mock)
    return future


@pytest.fixture
def return_none_future():
    future = asyncio.Future()
    future.set_result(None)
    return future
