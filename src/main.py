import streamlit as st

from presentation.streamlit.singletons.event_handlers.book import (
    get_book_event_handler,
)
from presentation.streamlit.singletons.logger import init_logger
from presentation.streamlit.singletons.pubsub import get_event_publisher
from presentation.streamlit.ui.create_book_form import create_book_form
from presentation.streamlit.ui.delete_book_form import delete_book_form
from presentation.streamlit.ui.list_books import list_books
from presentation.streamlit.ui.update_book_form import update_book_form

init_logger()


st.title("Books CRUD App")

event_publisher = get_event_publisher()
book_event_handler = get_book_event_handler()
event_publisher.add_subscriber(book_event_handler)


selected_operation = st.selectbox(
    "Select Operation",
    ["Create", "Update", "Delete"],
    key="crud_operation_select",
)


# Display form based on the selected operation
if selected_operation == "Create":
    create_book_form()
elif selected_operation == "Update":
    update_book_form()
elif selected_operation == "Delete":
    delete_book_form()

# Display table with all books
list_books()
