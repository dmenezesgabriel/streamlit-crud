import asyncio
from unittest.mock import MagicMock

import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import EventType
from src.core.use_cases.author import AuthorUseCases


class TestAuthorUseCaseGetAuthorByName:
    @pytest.mark.asyncio
    async def test_should_call_author_gateway_get_author_once(
        self,
        author_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
    ) -> None:

        author_gateway_mock.get_author_by_name.return_value = (
            return_author_future
        )

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.get_author_by_name(
            name=name, author_gateway=author_gateway_mock
        )

        author_gateway_mock.get_author_by_name.assert_called_once_with(name)

        assert author.name == name


class TestAuthorUseCaseCreateAuthor:
    @pytest.mark.asyncio
    async def test_should_call_author_gateway_create_author_once(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ) -> None:

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
    async def test_should_call_event_gateway_create_event_once(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ) -> None:

        author_gateway_mock.create_author.return_value = return_author_future
        event_gateway_mock.create_event.return_value = return_event_future

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.create_author(
            name=name,
            author_gateway=author_gateway_mock,
            event_gateway=event_gateway_mock,
        )

        await event_gateway_mock.create_event.called_once_with(
            event_type=EventType.CREATED,
            model_type="authors",
            model_id=author.id,
            payload={"old": {}, "new": author.to_dict()},
            event_gateway=event_gateway_mock,
        )

    @pytest.mark.asyncio
    async def test_should_return_author_instance(
        self,
        author_gateway_mock: MagicMock,
        event_gateway_mock: MagicMock,
        return_author_future: asyncio.Future,
        return_event_future: asyncio.Future,
    ) -> None:

        author_gateway_mock.create_author.return_value = return_author_future
        event_gateway_mock.create_event.return_value = return_event_future

        name = "J. R. R. Tolkien"
        author = await AuthorUseCases.create_author(
            name=name,
            author_gateway=author_gateway_mock,
            event_gateway=event_gateway_mock,
        )

        assert isinstance(author, AuthorEntity)
