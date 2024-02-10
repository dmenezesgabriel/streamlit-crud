from typing import List

import streamlit as st

from core.domain.entities.book import Book as BookEntity
from external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


@st.cache_resource
def get_books_list_cache() -> List[BookEntity]:
    book_controller = get_book_controller()
    return book_controller.get_books()
