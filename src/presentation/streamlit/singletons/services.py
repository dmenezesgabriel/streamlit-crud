import streamlit as st

from application.services.book import BookService
from presentation.streamlit.singletons.repositories import (
    get_author_repository,
    get_book_repository,
)


@st.cache_resource
def get_book_service():
    author_repository = get_author_repository()
    book_repository = get_book_repository()
    return BookService(book_repository, author_repository)
