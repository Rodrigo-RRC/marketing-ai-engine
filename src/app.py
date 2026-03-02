"""
Application entry point.
"""

import streamlit as st
st.write("APP INICIADO")

from dotenv import load_dotenv

from src.core.config import get_groq_api_key
from src.services.llm_service import initialize_llm
from src.ui.interface import render_interface


def main() -> None:

    st.set_page_config(
        page_title="Marketing AI Engine",
        layout = "wide",
        initial_sidebar_state="expanded"
        )

    load_dotenv()

    user_key = st.sidebar.text_input("Groq API Key", type="password")

    try:
        api_key = get_groq_api_key(user_key)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    llm = initialize_llm(api_key)

    render_interface(llm)


if __name__ == "__main__":
    main()