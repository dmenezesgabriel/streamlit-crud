import streamlit as st

from application.services.book import BookService
from infrastructure.database.sqlalchemy.orm import SessionLocal
from presentation.streamlit.ui.books_list import BooksList
from presentation.streamlit.ui.create_book_form import CreateBookForm
from presentation.streamlit.ui.delete_book_form import DeleteBookForm
from presentation.streamlit.ui.update_book_form import UpdateBookForm

st.title("Books CRUD App")

db = SessionLocal()

book_service = BookService(db)


def main():
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

    # Close the database session
    db.close()


main()
