import streamlit as st

from application.services.book import BookService
from application.services.event import EventService
from presentation.streamlit.singletons.pubsub import get_event_publisher
from presentation.streamlit.singletons.sqlalchemy.repositories import (
    get_author_repository,
    get_book_repository,
    get_event_repository,
)


@st.cache_resource
def get_book_service():
    author_repository = get_author_repository()
    book_repository = get_book_repository()
    event_publisher = get_event_publisher()
    return BookService(
        book_repository=book_repository,
        author_repository=author_repository,
        event_publisher=event_publisher,
    )


@st.cache_resource
def get_event_service():
    event_repository = get_event_repository()
    return EventService(event_repository)
