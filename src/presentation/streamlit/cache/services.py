import streamlit as st

from presentation.streamlit.singletons.services import get_book_service


@st.cache_resource
def get_books_list_cache():
    books_service = get_book_service()
    return books_service.get_books()
