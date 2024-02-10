from typing import List

import streamlit as st

from external.web.streamlit.cache.use_cases import get_books_list_cache
from external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


def _get_book_options() -> List[str]:
    return [f"{book.id}: {book.title}" for book in get_books_list_cache()]


def delete_book_form() -> None:
    with st.container(border=True):
        st.header("Delete Book")

        books_options = _get_book_options()

        # Selectbox to choose book for deletion
        book_id_to_delete = st.selectbox(
            "Select Book to Delete",
            [""] + books_options,
            key="delete_books_select",
        )

        # Display delete button if a book is selected
        if book_id_to_delete:
            with st.form("delete_book_form", border=False):
                book_id = book_id_to_delete.split(":")[0].strip()
                if st.form_submit_button("Delete"):
                    book_controller = get_book_controller()
                    book = book_controller.delete_book(
                        book_id=book_id,
                    )
                    get_books_list_cache.clear()
                    if book:
                        st.success(f"Book with ID {book.id} deleted!")
