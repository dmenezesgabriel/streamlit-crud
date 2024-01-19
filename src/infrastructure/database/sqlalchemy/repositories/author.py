from sqlalchemy.orm import Session

from infrastructure.database.sqlalchemy.models.author import (
    Author as AuthorModel,
)


class AuthorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_author_by_name(self, name: str) -> AuthorModel:
        author = self.db.query(AuthorModel).filter_by(name=name).first()
        if author:
            return author
        else:
            return None

    def create_author(self, name: str) -> AuthorModel:
        try:
            author = AuthorModel(name=name)
            self.db.add(author)
            self.db.commit()
            self.db.refresh(author)
            return author
        except Exception as error:
            self.db.rollback()
            raise error
