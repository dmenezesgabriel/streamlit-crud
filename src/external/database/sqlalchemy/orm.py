import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import QueuePool

load_dotenv()


class Base(AsyncAttrs, DeclarativeBase):
    pass


# Create SQLite database engine
DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_async_engine(
    DATABASE_URI, pool_size=5, max_overflow=0, poolclass=QueuePool
)


# Create a session to interact with the database
async_session = async_sessionmaker(
    expire_on_commit=False,
    bind=engine,
)
