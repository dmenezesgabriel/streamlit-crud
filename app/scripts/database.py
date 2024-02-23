import asyncio
import os
import sys

sys.path.append(os.getcwd())

from src.external.database.sqlalchemy.models.author import Author  # noqa
from src.external.database.sqlalchemy.models.base import Base  # noqa
from src.external.database.sqlalchemy.models.book import Book  # noqa
from src.external.database.sqlalchemy.models.event import Event  # noqa
from src.external.database.sqlalchemy.orm import engine  # noqa


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
