import pandas as pd
import streamlit as st

from presentation.streamlit.utils.dataframe import (
    get_dataframe_rows_added,
    get_dataframe_rows_cells_updated,
    get_dataframe_rows_removed,
)
from utils.identifiers import generate_uuid


class BooksList:
    def __init__(self, book_service):
        self.book_service = book_service

    def execute(self):
        st.header("List of Books")
        books = self.book_service.get_books()
        if books:
            books_data = {"ID": [], "Title": [], "Author": []}
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
            added_rows = get_dataframe_rows_added(
                books_df, edited_dataframe, "ID"
            )
            deleted_rows = get_dataframe_rows_removed(
                books_df, edited_dataframe, "ID"
            )

            with st.expander("Changed Data"):
                st.write("updated: ")
                st.json(updated_rows.to_json(orient="records"))
                st.write("added: ")
                st.json(added_rows.to_json(orient="records"))
                st.write("removed: ")
                st.json(deleted_rows.to_json(orient="records"))
