import streamlit as st
from src.external.web.streamlit.components.side_nav import side_nav


async def render() -> None:
    with st.sidebar:
        side_nav()

    st.header("Under construction")
