import streamlit as st

from external.web.streamlit.cache.use_cases import get_books_list_cache
from external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


async def create_book_form() -> None:
    with st.container(border=True):
        st.header("Create Book Form")
        with st.form("create_form", border=False):
            title = st.text_input("Title:")
            author_name = st.text_input("Author:")
            if st.form_submit_button("Create"):
                book_controller = get_book_controller()
                try:
                    book = await book_controller.create_book(
                        title=title,
                        author_name=author_name,
                    )
                    # await get_books_list_cache.clear()
                    st.success(
                        f"Book '{book.title}' by {book.author.name} "
                        "created!"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
