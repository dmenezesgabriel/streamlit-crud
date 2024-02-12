import logging

import streamlit as st
from external.logger.logger import configure_logger


@st.cache_resource
def init_logger() -> logging.Logger:
    return configure_logger()
