import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
Base = declarative_base()

# Create SQLite database engine
DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)


# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
