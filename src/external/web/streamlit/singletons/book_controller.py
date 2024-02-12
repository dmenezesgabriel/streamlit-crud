import streamlit as st

from communication.controllers.book import BookController
from external.database.sqlalchemy.repositories.author import AuthorRepository
from external.database.sqlalchemy.repositories.book import BookRepository
from external.database.sqlalchemy.repositories.event import EventRepository


@st.cache_resource
def get_book_controller():
    book_repository = BookRepository()
    author_repository = AuthorRepository()
    event_repository = EventRepository()
    book_controller = BookController(
        book_repository=book_repository,
        author_repository=author_repository,
        event_repository=event_repository,
    )
    return book_controller
