from uuid import UUID

import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.entities.book import Book as BookEntity
from src.core.domain.exceptions import (
    BookAuthorNotAuthorEntityInstance,
    BookTitleNotInformed,
)


@pytest.fixture
def author_mock() -> AuthorEntity:
    return AuthorEntity(name="J. R. R. Tolkien")


class TestBookEntity:
    def test_create_book(self, author_mock: AuthorEntity) -> None:
        book = BookEntity(
            title="The Fellowship of the Ring", author=author_mock
        )
        assert UUID(book.id, version=4)
        assert book

    @pytest.mark.parametrize("title", ["", None])
    def test_create_book_with_empty_title(
        self, author_mock: AuthorEntity, title: str
    ) -> None:
        with pytest.raises(BookTitleNotInformed):
            BookEntity(title=title, author=author_mock)

    @pytest.mark.parametrize("author_mock", [0, "John Doe", {}, [], True])
    def test_create_book_wrong_author_type(
        self, author_mock: AuthorEntity
    ) -> None:
        with pytest.raises(BookAuthorNotAuthorEntityInstance):
            BookEntity(title="The Fellowship of the Ring", author=author_mock)

    def test_book_to_dict(self, author_mock: AuthorEntity) -> None:
        book = BookEntity(
            title="The Fellowship of the Ring", author=author_mock
        )
        book_dict_attributes = book.to_dict()
        assert isinstance(book_dict_attributes, dict)
        assert book_dict_attributes["title"] == "The Fellowship of the Ring"
        assert book_dict_attributes["author"]["name"] == "J. R. R. Tolkien"
