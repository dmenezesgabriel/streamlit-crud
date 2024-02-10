import streamlit as st

from external.event_handlers.book import BookEventHandler


@st.cache_resource
def get_book_event_handler():
    return BookEventHandler()
