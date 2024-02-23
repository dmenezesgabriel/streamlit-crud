class BaseException(Exception):
    pass


class BadRequest(BaseException):
    status = 400


class NotFound(BaseException):
    status = 404
