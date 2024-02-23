from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import QueuePool
from src.config import get_config

load_dotenv()

config = get_config()

# Create SQLite database engine

engine = create_async_engine(
    config.DATABASE_URI, pool_size=5, max_overflow=0, poolclass=QueuePool
)


# Create a session to interact with the database
async_session = async_sessionmaker(
    expire_on_commit=False,
    bind=engine,
)
