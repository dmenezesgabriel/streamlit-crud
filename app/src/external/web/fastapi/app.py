from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.external.web.fastapi.api_v1.api import router as api_router
from src.external.web.fastapi.exception_handlers import register_exceptions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

register_exceptions(app)
