import asyncio
from typing import List

import streamlit as st
from aiocache import Cache, cached

from core.domain.entities.book import Book as BookEntity
from external.web.streamlit.singletons.book_controller import (
    get_book_controller,
)


@cached(ttl=None, cache=Cache.MEMORY)
async def get_books_list_cache() -> List[BookEntity]:
    book_controller = get_book_controller()
    return await book_controller.get_books()
