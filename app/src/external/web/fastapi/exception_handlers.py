from fastapi import FastAPI
from src.core.domain.exceptions import (
    AuthorNameNotInformed,
    BookAlreadyExists,
    BookAuthorNotAuthorEntityInstance,
    BookNotFound,
    BookTitleNotInformed,
    OperationalError,
)
from starlette.requests import Request
from starlette.responses import JSONResponse


def register_exceptions(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def validation_exception_handler(
        request: Request, err: Exception
    ) -> JSONResponse:
        base_error_message = (
            f"Failed to execute: {request.method}: {request.url}"
        )
        return JSONResponse(
            status_code=500,
            content={"message": f"{base_error_message}. Detail: {err}"},
        )

    @app.exception_handler(BookAlreadyExists)
    async def book_already_exists_exception_handler(
        request: Request, exc: BookAlreadyExists
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(BookAuthorNotAuthorEntityInstance)
    async def book_author_not_entity_author_entity_instance_exception_handler(
        request: Request, exc: BookAuthorNotAuthorEntityInstance
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(AuthorNameNotInformed)
    async def author_name_not_informed_exception_handler(
        request: Request, exc: AuthorNameNotInformed
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(BookTitleNotInformed)
    async def book_title_not_informed_exception_handler(
        request: Request, exc: BookTitleNotInformed
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(BookNotFound)
    async def book_title_not_found_handler(
        request: Request, exc: BookNotFound
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(OperationalError)
    async def operational_error_handler(
        request: Request, exc: OperationalError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )
