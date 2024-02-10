from typing import Dict


class AuthorNameNotInformed(Exception):
    def __init__(self, message: str, errors: Dict[str, str]):
        super().__init__(message)
        self.errors = error


class BookTitleNotInformed(Exception):
    def __init__(self, message: str, errors: Dict[str, str]):
        super().__init__(message)
        self.errors = error


class BookAuthorNotAuthorEntityInstance(Exception):
    def __init__(self, message: str, errors: Dict[str, str]):
        super().__init__(message)
        self.errors = error
