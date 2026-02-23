"""
LLM service module.
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def initialize_llm(api_key: str) -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        api_key=api_key,
    )


def generate_content(llm: ChatGroq, prompt: str) -> str:
    template = ChatPromptTemplate.from_messages([
        ("system", """
            Você é um Estrategista Sênior de Marketing Digital especializado em:

            - SEO avançado
            - Copywriting persuasivo
            - Psicologia do consumo
            - Estrutura AIDA e PAS
            - Estratégias de conversão e retenção

            REGRAS OBRIGATÓRIAS:

            1. Nunca produza conteúdo superficial.
            2. Sempre desenvolva argumentos com profundidade.
            3. Estruture o texto com subtítulos claros em Markdown.
            4. Integre palavras-chave naturalmente.
            5. Use técnicas reais de persuasão.
            6. Evite frases genéricas como “você já parou para pensar”.
            7. O conteúdo deve parecer escrito por um especialista humano experiente.

            CONTROLE DE PRECISÃO:

            8. Não estabeleça relações de causa e efeito entre fenômenos distintos sem base científica clara.
            9. Não misture problemas ambientais diferentes como se fossem consequência direta uns dos outros.
            10. Se não tiver certeza absoluta da relação causal, descreva como fenômenos correlacionados, não causais.
            11. Evite exageros ou afirmações científicas imprecisas.

            O texto precisa ser estratégico, profissional, preciso e pronto para publicação.
            """),
        ("human", "{prompt}")
    ])

    chain = template | llm | StrOutputParser()
    return chain.invoke({"prompt": prompt})