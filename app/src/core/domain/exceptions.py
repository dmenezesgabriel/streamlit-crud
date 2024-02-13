from typing import Dict


class OperationalError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class AuthorNameNotInformed(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BookTitleNotInformed(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BookAuthorNotAuthorEntityInstance(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BookAlreadyExists(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BookNotFound(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidEventType(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidModelId(Exception):
    def __init__(self, message: str):
        super().__init__(message)
