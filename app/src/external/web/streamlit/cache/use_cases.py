import asyncio
from typing import List

from aiocache import Cache, cached

import streamlit as st
from src.external.web.streamlit.singletons.book_controller import \
    get_book_controller
from src.core.domain.entities.book import Book as BookEntity


@cached(ttl=None, cache=Cache.MEMORY)
async def get_books_list_cache() -> List[BookEntity]:
    book_controller = get_book_controller()
    return await book_controller.get_books()
