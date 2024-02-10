import streamlit as st

from communication.controllers.book import BookController
from external.web.streamlit.cache.use_cases import get_books_list_cache


def create_book_form():
    with st.container(border=True):
        st.header("Create Book Form")
        with st.form("create_form", border=False):
            title = st.text_input("Title:")
            author_name = st.text_input("Author:")
            if st.form_submit_button("Create"):
                try:
                    book = BookController.create_book(
                        title=title,
                        author_name=author_name,
                    )
                    get_books_list_cache.clear()
                    st.success(
                        f"Book '{book.title}' by {book.author.name} "
                        "created!"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
