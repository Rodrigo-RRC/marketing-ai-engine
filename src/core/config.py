"""
Core configuration module.
Responsible for retrieving and validating environment configuration.
"""

from typing import Optional
import os


def get_groq_api_key(user_input: Optional[str]) -> str:
    """
    Retrieve Groq API key from environment or user input.
    """

    env_key: Optional[str] = os.getenv("GROQ_API_KEY")

    api_key: Optional[str] = env_key or user_input

    if not api_key:
        raise ValueError("GROQ API Key não fornecida.")

    return api_key