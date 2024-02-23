import asyncio
from typing import List
from unittest.mock import MagicMock

import pytest
from src.communication.gateway.author import AuthorGateway
from src.communication.gateway.book import BookGateway
from src.communication.gateway.event import EventGateway
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.book import Book as BookEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType


@pytest.fixture
def author_mock() -> AuthorEntity:
    return AuthorEntity(name="J. R. R. Tolkien")


@pytest.fixture
def book_mock(author_mock: MagicMock) -> BookEntity:
    return BookEntity(title="The Fellowship of the Ring", author=author_mock)


@pytest.fixture
def event_mock(author_mock: MagicMock) -> EventEntity:
    return EventEntity(
        event_type=EventType.CREATED,
        model_type="authors",
        model_id=author_mock.id,
        payload={"old": {}, "new": author_mock.to_dict()},
    )


@pytest.fixture
def book_list_mock(book_mock: MagicMock) -> List[EventEntity]:
    return [book_mock]


@pytest.fixture
def event_list_mock(event_mock: MagicMock) -> List[EventEntity]:
    return [event_mock]


@pytest.fixture
def author_gateway_mock() -> MagicMock:
    return MagicMock(spec=AuthorGateway)


@pytest.fixture
def book_gateway_mock() -> MagicMock:
    return MagicMock(spec=BookGateway)


@pytest.fixture
def event_gateway_mock() -> MagicMock:
    return MagicMock(spec=EventGateway)


@pytest.fixture
def return_author_future(
    author_mock: AuthorEntity,
) -> asyncio.Future[AuthorEntity]:
    future: asyncio.Future[AuthorEntity] = asyncio.Future()
    future.set_result(author_mock)
    return future


@pytest.fixture
def return_event_future(
    event_mock: EventEntity,
) -> asyncio.Future[EventEntity]:
    future: asyncio.Future[EventEntity] = asyncio.Future()
    future.set_result(event_mock)
    return future


@pytest.fixture
def return_none_future() -> asyncio.Future[None]:
    future: asyncio.Future[None] = asyncio.Future()
    future.set_result(None)
    return future
