import asyncio

import streamlit as st

from external.web.streamlit.singletons.logger import init_logger
from external.web.streamlit.ui.create_book_form import create_book_form
from external.web.streamlit.ui.delete_book_form import delete_book_form
from external.web.streamlit.ui.list_books import list_books
from external.web.streamlit.ui.update_book_form import update_book_form

st.set_page_config(layout="wide")


async def main():
    init_logger()

    st.title("Books CRUD App")

    selected_operation = st.selectbox(
        "Select Operation",
        ["Create", "Update", "Delete"],
        key="crud_operation_select",
    )

    # Display form based on the selected operation
    if selected_operation == "Create":
        await create_book_form()
    elif selected_operation == "Update":
        await update_book_form()
    elif selected_operation == "Delete":
        await delete_book_form()

    # Display table with all books
    await list_books()


if __name__ == "__main__":
    asyncio.run(main())
