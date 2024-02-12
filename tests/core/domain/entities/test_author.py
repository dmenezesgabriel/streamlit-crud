import pytest

from core.domain.entities.author import Author as AuthorEntity
from core.domain.exceptions import AuthorNameNotInformed


class TestAuthorEntity:
    def test_create_author(self):
        author = AuthorEntity(name="J. R. R. Tolkien")
        assert author

    @pytest.mark.parametrize("name", ["", None])
    def test_create_author_with_empty_name(self, name):
        with pytest.raises(AuthorNameNotInformed):
            AuthorEntity(name=name)
