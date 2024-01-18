import streamlit as st
from models import SessionLocal
from services import BookService
from sqlalchemy.exc import IntegrityError

st.title("Books CRUD App")

db = SessionLocal()

book_service = BookService(db)


def main():
    selected_operation = st.selectbox(
        "Select Operation", ["Create", "Update", "Delete"]
    )

    # Display form based on the selected operation
    if selected_operation == "Create":
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
                    except IntegrityError as e:
                        st.error(f"Error: {str(e)}")

    elif selected_operation == "Update":
        with st.container(border=True):
            st.header("Update Book")

            # Selectbox to choose book for updating
            book_id_to_update = st.selectbox(
                "Select Book to Update",
                [""]
                + [
                    f"{book.id}: {book.title}"
                    for book in book_service.get_books()
                ],
            )

            # Display form fields if a book is selected
            if book_id_to_update:
                with st.form("update_book_form", border=False):
                    book_id = int(book_id_to_update.split(":")[0])
                    selected_book = book_service.get_book(book_id)
                    title = st.text_input(
                        "New Title:", value=selected_book.title
                    )
                    author_name = st.text_input(
                        "New Author:", value=selected_book.author.name
                    )
                    if st.form_submit_button("Update"):
                        book = book_service.update_book(
                            book_id, title, author_name
                        )
                        if book:
                            st.success(f"Book with ID {book.id} updated!")

    elif selected_operation == "Delete":
        with st.container(border=True):
            st.header("Delete Book")

            # Selectbox to choose book for deletion
            book_id_to_delete = st.selectbox(
                "Select Book to Delete",
                [""]
                + [
                    f"{book.id}: {book.title}"
                    for book in book_service.get_books()
                ],
            )

            # Display delete button if a book is selected
            if book_id_to_delete:
                with st.form("delete_book_form", border=False):
                    book_id = int(book_id_to_delete.split(":")[0])
                    if st.form_submit_button("Delete"):
                        book = book_service.delete_book(book_id)
                        if book:
                            st.success(f"Book with ID {book.id} deleted!")

    # Display table with all books
    st.header("List of Books")
    books = book_service.get_books()
    if books:
        books_data = {"ID": [], "Title": [], "Author": []}
        for book in books:
            books_data["ID"].append(book.id)
            books_data["Title"].append(book.title)
            books_data["Author"].append(book.author.name)

        st.dataframe(books_data)
        # st.data_editor(books_data,key="data_editor", num_rows="dynamic")
        # st.write(st.session_state["data_editor"])

    # Close the database session
    db.close()


main()
