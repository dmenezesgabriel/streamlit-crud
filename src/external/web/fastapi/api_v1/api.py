from fastapi import APIRouter

from external.web.fastapi.api_v1.endpoints import book

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


router.include_router(book.router)