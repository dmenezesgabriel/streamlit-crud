import streamlit as st

from communication.controllers.book import BookController


@st.cache_resource
def get_books_list_cache():
    return BookController.get_books()
