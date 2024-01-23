import streamlit as st

from infrastructure.event_handlers.book import BookEventHandler
from presentation.streamlit.singletons.services import get_event_service


@st.cache_resource
def get_book_event_handler():
    event_service = get_event_service()
    return BookEventHandler(event_service=event_service)
