import streamlit as st

from external.web.streamlit.cache.use_cases import get_books_list_cache
from external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


async def update_book_form() -> None:
    with st.container(border=True):
        st.header("Update Book")

        # Selectbox to choose book for updating
        book_id_to_update = st.selectbox(
            "Select Book to Update",
            [""]
            + [
                f"{book.id}: {book.title}"
                for book in await get_books_list_cache()
            ],
            key="update_books_select",
        )

        # Display form fields if a book is selected
        if book_id_to_update:
            with st.form("update_book_form", border=False):
                book_id = book_id_to_update.split(":")[0].strip()
                book_controller = get_book_controller()
                selected_book = await book_controller.get_book(book_id)
                title = st.text_input("New Title:", value=selected_book.title)
                author_name = st.text_input(
                    "New Author:", value=selected_book.author.name
                )
                if st.form_submit_button("Update"):
                    book = await book_controller.update_book(
                        book_id=book_id,
                        title=title,
                        author_name=author_name,
                    )
                    # await get_books_list_cache.clear()
                    if book:
                        st.success(f"Book with ID {book.id} updated!")
