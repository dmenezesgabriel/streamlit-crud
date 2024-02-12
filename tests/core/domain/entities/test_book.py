import pytest

from core.domain.entities.author import Author as AuthorEntity
from core.domain.entities.book import Book as BookEntity
from core.domain.exceptions import (
    BookAuthorNotAuthorEntityInstance,
    BookTitleNotInformed,
)


@pytest.fixture
def author():
    return AuthorEntity(name="J. R. R. Tolkien")


class TestBookEntity:
    def test_create_book(self, author):
        book = BookEntity(title="The Fellowship of the Ring", author=author)
        assert book

    @pytest.mark.parametrize("title", ["", None])
    def test_create_book_with_empty_title(self, author, title):
        with pytest.raises(BookTitleNotInformed):
            BookEntity(title=title, author=author)

    @pytest.mark.parametrize("author", [0, "John Doe", {}, [], True])
    def test_create_book_wrong_author_type(self, author):
        with pytest.raises(BookAuthorNotAuthorEntityInstance):
            BookEntity(title="The Fellowship of the Ring", author=author)
