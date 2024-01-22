import streamlit as st


def update_book_form(book_service):
    with st.container(border=True):
        st.header("Update Book")

        # Selectbox to choose book for updating
        book_id_to_update = st.selectbox(
            "Select Book to Update",
            [""]
            + [
                f"{book.id}: {book.title}" for book in book_service.get_books()
            ],
            key="update_books_select",
        )

        # Display form fields if a book is selected
        if book_id_to_update:
            with st.form("update_book_form", border=False):
                book_id = book_id_to_update.split(":")[0].strip()
                selected_book = book_service.get_book(book_id)
                title = st.text_input("New Title:", value=selected_book.title)
                author_name = st.text_input(
                    "New Author:", value=selected_book.author.name
                )
                if st.form_submit_button("Update"):
                    book = book_service.update_book(
                        book_id, title, author_name
                    )
                    if book:
                        st.success(f"Book with ID {book.id} updated!")
