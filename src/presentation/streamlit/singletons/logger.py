import streamlit as st

from infrastructure.logger.logger import configure_logger


@st.cache_resource
def init_logger():
    return configure_logger()
