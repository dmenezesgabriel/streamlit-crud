import streamlit as st

from infrastructure.pubsub.pubsub import EventPublisher


@st.cache_resource
def get_event_publisher():
    return EventPublisher()
