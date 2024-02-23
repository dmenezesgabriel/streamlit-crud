import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import QueuePool

load_dotenv()


# Create SQLite database engine
DATABASE_URI = str(os.getenv("DATABASE_URI"))
engine = create_async_engine(
    DATABASE_URI, pool_size=5, max_overflow=0, poolclass=QueuePool
)


# Create a session to interact with the database
async_session = async_sessionmaker(
    expire_on_commit=False,
    bind=engine,
)
