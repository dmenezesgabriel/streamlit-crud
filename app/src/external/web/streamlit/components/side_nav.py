import streamlit as st


def side_nav() -> None:
    st.page_link("init_streamlit.py", label="Home", icon="🏠")
    st.page_link("pages/page_2.py", label="Under construction", icon="🚧")
