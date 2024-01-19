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

            st.dataframe(books_data)
