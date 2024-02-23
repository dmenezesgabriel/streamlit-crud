import asyncio
import logging

import streamlit as st
from src.config import get_config
from src.external.web.streamlit.ui.create_book_form import create_book_form
from src.external.web.streamlit.ui.delete_book_form import delete_book_form
from src.external.web.streamlit.ui.list_books import list_books
from src.external.web.streamlit.ui.update_book_form import update_book_form

config = get_config()
logger = logging.getLogger(__name__)

st.set_page_config(layout="wide")


async def main() -> None:
    logger.info("runned main page")

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
