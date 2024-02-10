from typing import List

import streamlit as st

from communication.controllers.book import BookController
from core.domain.entities.book import Book as BookEntity


@st.cache_resource
def get_books_list_cache() -> List[BookEntity]:
    return BookController.get_books()
