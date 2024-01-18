import uuid

from db import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


def generate_uuid():
    return str(uuid.uuid4())


class Author(Base):
    __tablename__ = "authors"
    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    name = Column(String, index=True, unique=True)
    books = relationship("Book", back_populates="author")
