"""
Prompt builder module.
"""

from models.request_model import ContentRequest


def build_content_prompt(data: ContentRequest) -> str:
    """
    Build strategic marketing prompt with flexible structure.
    """

    primary_keyword = data.keywords if data.keywords else data.topic

    cta_section = ""
    if data.include_cta:
        cta_section = """
Inclua uma chamada para ação clara e estratégica ao final do conteúdo,
orientando o leitor para um próximo passo lógico.
"""

    hashtags_section = ""
    if data.include_hashtags:
        hashtags_section = """
Ao final do conteúdo, inclua entre 5 e 10 hashtags relevantes e estratégicas
relacionadas ao tema e à plataforma.
"""

    emoji_rule = (
        "Use emojis com moderação estratégica quando fizer sentido para a plataforma."
        if data.include_emojis
        else "Não utilize emojis."
    )

    return f"""
TEMA PRINCIPAL
{data.topic}

CONTEXTO DO CONTEÚDO

Plataforma: {data.platform}
Tom de comunicação: {data.tone}
Público-alvo: {data.audience}
Tamanho desejado: {data.length}

Palavra-chave principal:
{primary_keyword}

Objetivo estratégico do conteúdo:
{data.strategic_goal}

ADAPTAÇÃO DE TOM

O estilo do texto deve respeitar o tom selecionado:

Informativo:
priorize clareza, explicação objetiva e autoridade técnica.

Inspirador:
utilize linguagem mais envolvente, reflexiva e motivacional.

Formal:
adote estilo institucional, analítico e profissional.

DIRETRIZES DE QUALIDADE

• Escreva como um especialista no tema.
• Desenvolva ideias com profundidade e coerência.
• Evite superficialidade e frases genéricas.
• Priorize densidade informativa e clareza conceitual.

Sempre que possível:

• utilize dados amplamente reconhecidos
• mencione instituições, pesquisas ou estudos confiáveis
• inclua exemplos concretos ou situações reais
• explique mecanismos ou processos relevantes
• evite afirmações vagas ou sem fundamento

ESTRUTURA DO CONTEÚDO

O conteúdo deve possuir:

• um título claro e forte
• subtítulos naturais ao longo do texto
• parágrafos bem desenvolvidos
• progressão lógica das ideias

A organização pode incluir, quando fizer sentido:

introdução do tema  
contextualização e relevância atual  
explicações ou análises mais profundas  
exemplos práticos ou aplicações reais  
implicações estratégicas ou reflexões finais  

Evite estruturas rígidas ou previsíveis.

SEO

Utilize a palavra-chave principal de forma natural ao longo do texto.
Evite repetição artificial e priorize fluidez na leitura.

DIRETRIZES ADICIONAIS

{emoji_rule}

Evite:

• clichês
• frases genéricas
• generalizações superficiais
• conteúdo inflado sem valor informativo

{cta_section}

{hashtags_section}
"""