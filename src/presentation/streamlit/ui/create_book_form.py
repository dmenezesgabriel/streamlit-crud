import streamlit as st

from controllers.book import BookController
from presentation.streamlit.cache.use_cases import get_books_list_cache
from presentation.streamlit.singletons.pubsub import get_event_publisher


def create_book_form():
    with st.container(border=True):
        st.header("Create Book Form")
        with st.form("create_form", border=False):
            title = st.text_input("Title:")
            author_name = st.text_input("Author:")
            if st.form_submit_button("Create"):
                event_publisher = get_event_publisher()
                try:
                    book = BookController.create_book(
                        title=title,
                        author_name=author_name,
                        event_publisher=event_publisher,
                    )
                    get_books_list_cache.clear()
                    st.success(
                        f"Book '{book.title}' by {book.author.name} "
                        "created!"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
