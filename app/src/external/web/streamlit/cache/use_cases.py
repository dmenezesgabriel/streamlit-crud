from typing import List

from aiocache import Cache, cached
from src.core.domain.entities.book import Book as BookEntity
from src.external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


@cached(ttl=None, cache=Cache.MEMORY)  # type: ignore
async def get_books_list_cache() -> List[BookEntity]:
    book_controller = get_book_controller()
    return await book_controller.get_books()
