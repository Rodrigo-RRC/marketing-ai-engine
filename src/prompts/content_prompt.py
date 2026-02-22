"""
Prompt builder module.
"""

from models.request_model import ContentRequest


def build_content_prompt(data: ContentRequest) -> str:
    """
    Build structured prompt from validated request.
    """

    return f"""
    Escreva um título sobre "{data.topic}".
    Escreva um texto otimizado para SEO.
    Linguagem formal e persuasiva.
    Retorne apenas o texto final.

    Plataforma: {data.platform}
    Tom: {data.tone}
    Público: {data.audience}
    Tamanho: {data.length}
    {"Inclua CTA." if data.include_cta else "Sem CTA."}
    {"Inclua hashtags." if data.include_hashtags else "Sem hashtags."}
    {"Inclua emojis moderados." if data.include_emojis else "Sem emojis."}
    {f"Palavras-chave obrigatórias: {data.keywords}" if data.keywords else ""}
    """