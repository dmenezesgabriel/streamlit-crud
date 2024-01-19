import streamlit as st


class DeleteBookForm:
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        with st.container(border=True):
            st.header("Delete Book")

            # Selectbox to choose book for deletion
            book_id_to_delete = st.selectbox(
                "Select Book to Delete",
                [""]
                + [
                    f"{book.id}: {book.title}"
                    for book in self.book_service.get_books()
                ],
            )

            # Display delete button if a book is selected
            if book_id_to_delete:
                with st.form("delete_book_form", border=False):
                    book_id = book_id_to_delete.split(":")[0].strip()
                    if st.form_submit_button("Delete"):
                        book = self.book_service.delete_book(book_id)
                        if book:
                            st.success(f"Book with ID {book.id} deleted!")
