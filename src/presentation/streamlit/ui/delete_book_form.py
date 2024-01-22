import streamlit as st


def delete_book_form(book_service):
    with st.container(border=True):
        st.header("Delete Book")

        # Selectbox to choose book for deletion
        book_id_to_delete = st.selectbox(
            "Select Book to Delete",
            [""]
            + [
                f"{book.id}: {book.title}" for book in book_service.get_books()
            ],
            key="delete_books_select",
        )

        # Display delete button if a book is selected
        if book_id_to_delete:
            with st.form("delete_book_form", border=False):
                book_id = book_id_to_delete.split(":")[0].strip()
                if st.form_submit_button("Delete"):
                    book = book_service.delete_book(book_id)
                    if book:
                        st.success(f"Book with ID {book.id} deleted!")
