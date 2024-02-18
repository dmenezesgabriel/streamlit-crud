import asyncio
from unittest.mock import MagicMock

import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import Event as EventEntity
from src.core.domain.entities.event import EventType
from src.core.use_cases.author import AuthorUseCases


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
def author_gateway_mock() -> MagicMock:
    return MagicMock()


@pytest.fixture
def event_gateway_mock() -> MagicMock:
    return MagicMock()


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


class TestAuthorUseCase:
    @pytest.mark.asyncio
    async def test_get_author_by_name_call_author_gateway_get_author_once(
        self,
        author_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
    ):

        author_gateway_mock.get_author_by_name.return_value = (
            return_author_future
        )

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.get_author_by_name(
            name=name, author_gateway=author_gateway_mock
        )

        author_gateway_mock.get_author_by_name.assert_called_once_with(name)

        assert author.name == name

    @pytest.mark.asyncio
    async def test_create_author_call_author_gateway_create_author_once(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ):

        author_gateway_mock.create_author.return_value = return_author_future
        event_gateway_mock.create_event.return_value = return_event_future

        name = "J. R. R. Tolkien"
        await AuthorUseCases.create_author(
            name=name,
            author_gateway=author_gateway_mock,
            event_gateway=event_gateway_mock,
        )

        author_gateway_mock.create_author.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_author_call_event_gateway_create_event_once(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ):

        author_gateway_mock.create_author.return_value = return_author_future
        event_gateway_mock.create_event.return_value = return_event_future

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.create_author(
            name=name,
            author_gateway=author_gateway_mock,
            event_gateway=event_gateway_mock,
        )

        event_gateway_mock.create_event.called_once_with(
            event_type=EventType.CREATED,
            model_type="authors",
            model_id=author.id,
            payload={"old": {}, "new": author.to_dict()},
            event_gateway=event_gateway_mock,
        )

    @pytest.mark.asyncio
    async def test_create_author_return_author_instance(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ):

        author_gateway_mock.create_author.return_value = return_author_future
        event_gateway_mock.create_event.return_value = return_event_future

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.create_author(
            name=name,
            author_gateway=author_gateway_mock,
            event_gateway=event_gateway_mock,
        )

        assert isinstance(author, AuthorEntity)
