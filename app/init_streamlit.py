import asyncio

from src.external.web.streamlit.views.home import render

if __name__ == "__main__":
    asyncio.run(render())
