"""
Streamlit UI layer.
"""

import streamlit as st
from pydantic import ValidationError

from models.request_model import ContentRequest
from prompts.content_prompt import build_content_prompt
from services.llm_service import generate_content



def render_interface(llm) -> None:

    st.title("Marketing AI Engine")

    topic = st.text_input(
                "Tema",
                placeholder="Ex: Saúde mental no ambiente corporativo, Marketing para clínicas odontológicas..."
            )
    platform = st.selectbox("Plataforma", ["Instagram", "LinkedIn", "Blog"])
    tone = st.selectbox("Tom", ["Informativo", "Inspirador", "Formal"])
    audience = st.selectbox("Público", ["Geral", "Profissionais", "Empresas"])
    length = st.selectbox("Tamanho", ["Curto", "Médio", "Longo"])

    include_cta = st.checkbox("Incluir CTA")
    include_hashtags = st.checkbox("Incluir hashtags")
    include_emojis = st.checkbox("Incluir emojis")

    keywords = st.text_area(
                "Palavras-chave",
                placeholder="Ex: saúde mental, produtividade, bem-estar no trabalho, ansiedade corporativa"
            )
    
    strategic_goal = st.selectbox(
            "Objetivo Estratégico",
            ["Autoridade", "Conversão", "Engajamento", "Educação de Mercado"]
        )

    if st.button("Gerar conteúdo"):

        try:
            request = ContentRequest(
            topic=topic,
            platform=platform,
            tone=tone,
            audience=audience,
            length=length,
            include_cta=include_cta,
            include_hashtags=include_hashtags,
            include_emojis=include_emojis,
            keywords=keywords,
            strategic_goal=strategic_goal
         )

            prompt = build_content_prompt(request)

            with st.spinner("Gerando..."):
                result = generate_content(llm, prompt)

            st.markdown(result)

        except ValidationError as e:
            st.error(f"Erro de validação: {e}")