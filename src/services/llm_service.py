"""
LLM service module.
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def initialize_llm(api_key: str) -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        api_key=api_key,
    )


def generate_content(llm: ChatGroq, prompt: str) -> str:
    template = ChatPromptTemplate.from_messages([
        ("system", "Você é especialista em marketing digital."),
        ("human", "{prompt}")
    ])

    chain = template | llm | StrOutputParser()
    return chain.invoke({"prompt": prompt})