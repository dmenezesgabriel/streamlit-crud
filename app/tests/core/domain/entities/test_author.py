from uuid import UUID

import pytest
from src.core.domain.entities.author import Author as AuthorEntity
from src.core.domain.exceptions import AuthorNameNotInformed


class TestAuthorEntity:
    def test_create_author(self) -> None:
        author = AuthorEntity(name="J. R. R. Tolkien")
        assert author
        assert UUID(author.id, version=4)

    @pytest.mark.parametrize("name", ["", None])
    def test_create_author_with_empty_name(self, name: str) -> None:
        with pytest.raises(AuthorNameNotInformed):
            AuthorEntity(name=name)

    def test_book_to_dict(self) -> None:
        author = AuthorEntity(name="J. R. R. Tolkien")
        author_dict_attributes = author.to_dict()
        assert isinstance(author_dict_attributes, dict)
        assert author_dict_attributes["name"] == "J. R. R. Tolkien"
