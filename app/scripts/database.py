import asyncio
import os
import sys

sys.path.append(os.getcwd())

from src.external.database.sqlalchemy.models.author import Author
from src.external.database.sqlalchemy.models.base import Base
from src.external.database.sqlalchemy.models.book import Book
from src.external.database.sqlalchemy.models.event import Event
from src.external.database.sqlalchemy.orm import engine


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
