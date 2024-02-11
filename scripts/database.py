import asyncio
import sys

sys.path.append("src")

from external.database.sqlalchemy.models.author import Author
from external.database.sqlalchemy.models.book import Book
from external.database.sqlalchemy.models.event import Event
from external.database.sqlalchemy.orm import Base, engine


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
