from typing import Any, Optional, Type

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.external.database.sqlalchemy.orm import async_session


class DatabaseSessionMixin:
    """Database session mixin."""

    async def __aenter__(self) -> AsyncSession:
        self.session = async_session()
        return self.session

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> None:
        try:
            if exc_type is not None:
                await self.session.rollback()
        except SQLAlchemyError:
            pass
        finally:
            await self.session.close()


def use_database_session() -> DatabaseSessionMixin:
    return DatabaseSessionMixin()
