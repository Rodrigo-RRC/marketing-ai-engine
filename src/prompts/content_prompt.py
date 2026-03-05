def build_content_prompt(data: ContentRequest) -> str:
    """
    Build structured and strategic marketing prompt.
    """

    primary_keyword = data.keywords if data.keywords else data.topic

    cta_section = ""
    if data.include_cta:
        cta_section = "## Chamada para Ação\n- Crie um CTA forte, específico e direcionado."

    hashtags_section = ""
    if data.include_hashtags:
        hashtags_section = "## Hashtags\n- Liste hashtags estratégicas e relevantes (Mínimo 5 Hashtags e no Máximo 10)."

    emoji_rule = "Use emojis com moderação estratégica." if data.include_emojis else "Não use emojis."

    return f"""
Objetivo:
Criar conteúdo estratégico, persuasivo e otimizado para SEO sobre "{data.topic}".

Contexto:
- Plataforma: {data.platform}
- Tom: {data.tone}
- Público-alvo: {data.audience}
- Tamanho: {data.length}

Palavra-chave principal:
{primary_keyword}

Objetivo Estratégico:
{data.strategic_goal}

Adapte o conteúdo para cumprir esse objetivo:
- Autoridade → enfatize domínio técnico, profundidade e dados.
- Conversão → priorize persuasão, urgência e benefício claro.
- Engajamento → maximize identificação emocional.
- Educação de Mercado → explique conceitos com clareza e didática.

Obrigatório:
- Linguagem técnica e assertiva.
- Utilize dados amplamente reconhecidos quando forem consenso público.
- Quando usar números, priorize estatísticas consolidadas e não especulativas.
- Caso não haja dado confiável, use linguagem qualitativa estratégica.
- Não estabeleça relações causais sem base explícita.
- Alta densidade informativa.

ESTRUTURA OBRIGATÓRIA DE SAÍDA (Não precisam usar exatamente estes subtítulos em Markdown):
__Lembre-se que você está elaborando conteúdo para ser usado com Marketing__
# Título SEO Otimizado

## Introdução
- Inicie com dado, tensão ou promessa forte.
- Integre a palavra-chave no primeiro parágrafo.

## Contextualização Estratégica
- Explique relevância atual.
- Mostre impacto concreto.
- Demonstre autoridade.

## Desenvolvimento Profundo
- Argumentação estruturada.
- Técnicas reais de persuasão.
- Evite superficialidade.

## Aplicação Prática
- Ações concretas e executáveis.
- Valor prático claro.

## Conclusão Estratégica
- Síntese com posicionamento forte.
- Gere reflexão ou senso de urgência.

{cta_section}

{hashtags_section}

Regras adicionais:
{emoji_rule}
Evite clichês.
Evite generalizações vagas.
Evite texto excessivamente genérico.
"""