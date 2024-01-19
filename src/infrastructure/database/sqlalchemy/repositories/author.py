from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)
from infrastructure.database.sqlalchemy.session_mixing import (
    use_database_session,
)


class AuthorRepository:
    def get_author_by_name(self, name: str) -> AuthorModel:
        with use_database_session() as db:
            author = db.query(AuthorModel).filter_by(name=name).first()
            if author:
                return author
            else:
                return None

    def create_author(self, name: str) -> AuthorModel:
        with use_database_session() as db:
            author = AuthorModel(name=name)
            db.add(author)
            db.commit()
            db.refresh(author)
            return author
