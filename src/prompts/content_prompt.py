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
foco em clareza, explicação objetiva e autoridade técnica.

Inspirador:
linguagem mais envolvente, motivacional e emocional.

Formal:
estilo mais institucional, analítico e profissional.

DIRETRIZES DE QUALIDADE

• Escreva como um especialista no tema.  
• Desenvolva ideias com profundidade.  
• Evite superficialidade e frases genéricas.  
• Priorize clareza, coerência e densidade informativa.  

Sempre que possível:

• utilize dados amplamente reconhecidos  
• mencione instituições ou fontes confiáveis  
• evite afirmações sem fundamento claro  

ESTRUTURA DO CONTEÚDO

O conteúdo deve possuir:

• um título forte e claro  
• subtítulos naturais ao longo do texto  
• parágrafos bem desenvolvidos  
• progressão lógica das ideias  

A organização pode incluir, quando fizer sentido:

introdução do tema  
contextualização e relevância  
explicações ou análises aprofundadas  
exemplos ou aplicações práticas  
reflexões ou recomendações finais  

Evite estruturas rígidas ou previsíveis.

SEO

Utilize a palavra-chave principal de forma natural ao longo do texto.
Evite repetição artificial.

DIRETRIZES ADICIONAIS

{emoji_rule}

Evite:

• clichês  
• generalizações vagas  
• conteúdo superficial  
• repetição excessiva  

{cta_section}

{hashtags_section}
"""