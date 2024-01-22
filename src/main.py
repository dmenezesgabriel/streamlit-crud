import streamlit as st

from infrastructure.logger.logger import logger_instance
from presentation.streamlit.singletons.services import get_book_service
from presentation.streamlit.ui.books_list import BooksList
from presentation.streamlit.ui.create_book_form import CreateBookForm
from presentation.streamlit.ui.delete_book_form import DeleteBookForm
from presentation.streamlit.ui.update_book_form import UpdateBookForm

logger = logger_instance.get_logger()

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
    create_book_form = CreateBookForm(book_service)
    create_book_form.execute()

elif selected_operation == "Update":
    update_book_form = UpdateBookForm(book_service)
    update_book_form.execute()

elif selected_operation == "Delete":
    delete_book_form = DeleteBookForm(book_service)
    delete_book_form.execute()

# Display table with all books
books_list = BooksList(book_service)
books_list.execute()
