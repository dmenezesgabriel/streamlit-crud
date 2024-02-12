import asyncio
import os

import streamlit as st
from external.logger.logger import get_logger
from external.web.streamlit.ui.create_book_form import create_book_form
from external.web.streamlit.ui.delete_book_form import delete_book_form
from external.web.streamlit.ui.list_books import list_books
from external.web.streamlit.ui.update_book_form import update_book_form

st.set_page_config(layout="wide")


async def main() -> None:
    get_logger()

    st.title("Books CRUD App")

    tab1, tab2, tab3 = st.tabs(["Create", "Update", "Delete"])

    with tab1:
        await create_book_form()
    with tab2:
        await update_book_form()
    with tab3:
        await delete_book_form()

    await list_books()


if __name__ == "__main__":
    asyncio.run(main())
