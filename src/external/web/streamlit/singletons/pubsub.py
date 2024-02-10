import streamlit as st

from external.pubsub.publisher import EventPublisher


@st.cache_resource
def get_event_publisher():
    return EventPublisher()
