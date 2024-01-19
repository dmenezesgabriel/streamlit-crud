from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from infrastructure.database.sqlalchemy.orm import SessionLocal


class DatabaseSessionMixin:
    """Database session mixin."""

    def __enter__(self) -> Session:
        self.db = SessionLocal()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is not None:
                self.db.rollback()
        except SQLAlchemyError:
            pass
        finally:
            self.db.close()


def use_database_session():
    return DatabaseSessionMixin()
