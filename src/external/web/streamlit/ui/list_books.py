from typing import Dict, List

import pandas as pd

import streamlit as st
from external.web.streamlit.cache.use_cases import get_books_list_cache
from external.web.streamlit.utils.dataframe import (
    get_dataframe_rows_added, get_dataframe_rows_cells_updated,
    get_dataframe_rows_removed)


async def list_books() -> None:
    st.header("List of Books")
    books = await get_books_list_cache()
    if books:
        books_data: Dict[str, List[str]] = {
            "ID": [],
            "Title": [],
            "Author": [],
        }
        for book in books:
            books_data["ID"].append(book.id)
            books_data["Title"].append(book.title)
            books_data["Author"].append(book.author.name)

        # st.dataframe(books_data)

        books_df = pd.DataFrame(books_data)
        with st.form("dataframe_form"):
            edited_dataframe = st.data_editor(
                books_df,
                column_config={
                    "ID": st.column_config.TextColumn(disabled=True),
                },
                key="data_editor",
                # num_rows="dynamic",
            )
            st.form_submit_button("Save", type="primary")

        # Identify rows where any cell has changed
        updated_rows = get_dataframe_rows_cells_updated(
            books_df, edited_dataframe, "ID"
        )
        added_rows = get_dataframe_rows_added(books_df, edited_dataframe, "ID")
        deleted_rows = get_dataframe_rows_removed(
            books_df, edited_dataframe, "ID"
        )

        with st.expander("Changed Data"):
            st.write("updated: ")
            st.json(updated_rows.to_dict(orient="records"))
            st.write("added: ")
            st.json(added_rows.to_dict(orient="records"))
            st.write("removed: ")
            st.json(deleted_rows.to_dict(orient="records"))
