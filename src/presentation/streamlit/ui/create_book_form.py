import streamlit as st


def create_book_form(book_service):
    with st.container(border=True):
        st.header("Create Book Form")
        with st.form("create_form", border=False):
            title = st.text_input("Title:")
            author_name = st.text_input("Author:")
            if st.form_submit_button("Create"):
                try:
                    book = book_service.create_book(title, author_name)
                    st.success(
                        f"Book '{book.title}' by {book.author.name} "
                        "created!"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
