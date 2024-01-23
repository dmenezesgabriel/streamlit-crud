import streamlit as st


def _get_book_options(get_books_list_cache):
    return [f"{book.id}: {book.title}" for book in get_books_list_cache()]


def delete_book_form(book_service, get_books_list_cache):
    with st.container(border=True):
        st.header("Delete Book")

        books_options = _get_book_options(get_books_list_cache)

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
                    book = book_service.delete_book(book_id)
                    get_books_list_cache.clear()
                    if book:
                        st.success(f"Book with ID {book.id} deleted!")
