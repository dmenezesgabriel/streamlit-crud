import logging

import streamlit as st

from presentation.streamlit.cache.services import get_books_list_cache
from presentation.streamlit.singletons.logger import init_logger
from presentation.streamlit.singletons.services import get_book_service
from presentation.streamlit.ui.create_book_form import create_book_form
from presentation.streamlit.ui.delete_book_form import delete_book_form
from presentation.streamlit.ui.list_books import list_books
from presentation.streamlit.ui.update_book_form import update_book_form

init_logger()

logger = logging.getLogger("app")

logger.info("runned main page")

st.title("Books CRUD App")


book_service = get_book_service()

selected_operation = st.selectbox(
    "Select Operation",
    ["Create", "Update", "Delete"],
    key="crud_operation_select",
)


# Display form based on the selected operation
if selected_operation == "Create":
    create_book_form(book_service, get_books_list_cache)
elif selected_operation == "Update":
    update_book_form(book_service, get_books_list_cache)
elif selected_operation == "Delete":
    delete_book_form(book_service, get_books_list_cache)

# Display table with all books
list_books(get_books_list_cache)
