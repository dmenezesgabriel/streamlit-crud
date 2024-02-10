import streamlit as st

from external.logger.logger import configure_logger


@st.cache_resource
def init_logger():
    return configure_logger()
