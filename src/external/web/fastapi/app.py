from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from core.domain.exceptions import (
    AuthorNameNotInformed,
    BookAlreadyExists,
    BookAuthorNotAuthorEntityInstance,
    BookTitleNotInformed,
)
from external.web.fastapi.api_v1.api import router as api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(
        status_code=500,
        content={"message": f"{base_error_message}. Detail: {err}"},
    )


@app.exception_handler(BookAlreadyExists)
async def unicorn_exception_handler(request: Request, exc: BookAlreadyExists):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(BookAuthorNotAuthorEntityInstance)
async def unicorn_exception_handler(
    request: Request, exc: BookAuthorNotAuthorEntityInstance
):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(AuthorNameNotInformed)
async def unicorn_exception_handler(
    request: Request, exc: AuthorNameNotInformed
):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(BookTitleNotInformed)
async def unicorn_exception_handler(
    request: Request, exc: BookTitleNotInformed
):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
