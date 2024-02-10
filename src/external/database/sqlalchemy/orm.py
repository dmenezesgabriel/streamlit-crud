import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()


class Base(DeclarativeBase):
    pass


# Create SQLite database engine
DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(
    DATABASE_URI, pool_size=5, max_overflow=0, poolclass=QueuePool
)


# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
