import streamlit as st

from infrastructure.database.sqlalchemy.repositories.author import (
    AuthorRepository,
)
from infrastructure.database.sqlalchemy.repositories.books import (
    BookRepository,
)
from infrastructure.database.sqlalchemy.repositories.event import (
    EventRepository,
)


@st.cache_resource
def get_book_repository():
    return BookRepository()


@st.cache_resource
def get_author_repository():
    return AuthorRepository()


@st.cache_resource
def get_event_repository():
    return EventRepository()
