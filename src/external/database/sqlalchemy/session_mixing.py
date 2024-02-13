from sqlalchemy.exc import SQLAlchemyError

from external.database.sqlalchemy.orm import async_session


class DatabaseSessionMixin:
    """Database session mixin."""

    async def __aenter__(self) -> async_session:
        self.session = async_session()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is not None:
                await self.session.rollback()
        except SQLAlchemyError:
            pass
        finally:
            await self.session.close()


def use_database_session() -> DatabaseSessionMixin:
    return DatabaseSessionMixin()
