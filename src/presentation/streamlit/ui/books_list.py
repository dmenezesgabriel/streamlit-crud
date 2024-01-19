import pandas as pd
import streamlit as st


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

            edited_dataframe = st.data_editor(
                books_df,
                column_config={
                    "ID": st.column_config.TextColumn(disabled=True)
                },
                key="data_editor",
                # num_rows="dynamic",
            )

            books_df = books_df.reset_index(drop=True)
            edited_dataframe = edited_dataframe.reset_index(drop=True)

            # Identify rows where any cell has changed
            changed_rows = books_df[(books_df != edited_dataframe).any(axis=1)]

            with st.expander("Changed Data"):
                st.json(changed_rows.to_json(orient="records"))
