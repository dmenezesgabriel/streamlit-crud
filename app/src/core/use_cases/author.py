from typing import Union

from src.common.interfaces.author_gateway import AuthorGatewayInterface
from src.common.interfaces.event_gateway import EventGatewayInterface
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.event import EventType
from src.core.use_cases.event import EventUseCase


class AuthorUseCases:
    @staticmethod
    async def get_author_by_name(
        name: str,
        author_gateway: AuthorGatewayInterface,
    ) -> Union[AuthorEntity, None]:
        return await author_gateway.get_author_by_name(name)

    @staticmethod
    async def create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
        event_gateway: EventGatewayInterface,
    ) -> AuthorEntity:
        author = AuthorEntity(name=name)

        author = await author_gateway.create_author(author)

        await EventUseCase.create_event(
            event_type=EventType.CREATED,
            model_type="authors",
            model_id=author.id,
            payload={"old": {}, "new": author.to_dict()},
            event_gateway=event_gateway,
        )
        return author

    @staticmethod
    async def get_or_create_author(
        name: str,
        author_gateway: AuthorGatewayInterface,
        event_gateway: EventGatewayInterface,
    ) -> AuthorEntity:
        existing_author = await AuthorUseCases.get_author_by_name(
            name=name,
            author_gateway=author_gateway,
        )

        if existing_author:
            author = existing_author
        else:
            author = await AuthorUseCases.create_author(
                name=name,
                author_gateway=author_gateway,
                event_gateway=event_gateway,
            )
        return author
