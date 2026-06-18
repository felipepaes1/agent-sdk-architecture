# Arquitetura

Este starter separa as partes que mudam com frequência das partes que sustentam o runtime.
O público da palestra deve conseguir clonar o repositório e editar primeiro os prompts e tools,
sem precisar entender toda a orquestração.

```text
.
├── prompts/                         # Prompts editáveis sem tocar no código
├── evals/                           # Casos pequenos para comparar mudanças
├── src/summit_agents/
│   ├── agents/                      # Definição e composição de agentes
│   ├── guardrails/                  # Futuras validações e políticas
│   ├── integrations/                # MCP, sessões, APIs externas
│   ├── tools/                       # Function tools e registry
│   └── workflows/                   # Como os agentes são executados
├── tests/                           # Testes locais pequenos
└── data/                            # Estado local ignorado pelo git
```

## Princípios

- Comece com um agente focado e adicione especialistas só quando houver diferença real de
  prompt, política, tool surface ou contrato de saída.
- Mantenha prompts em Markdown para facilitar edição durante workshops.
- Coloque a maior parte da semântica da tool na docstring da própria função.
- Use sessões quando quiser memória local controlada pela aplicação.
- Deixe tracing ligado enquanto estiver depurando prompts, handoffs e chamadas de tools.
- Registre exemplos em `evals/` sempre que ajustar prompts, roteamento ou tools.

## Adicionar uma tool

Edite `src/summit_agents/tools/custom.py`:

```python
from agents import function_tool


@function_tool
def consultar_catalogo(produto: str) -> str:
    """Consulta informações públicas sobre um produto no catálogo interno."""
    return f"Resultado de exemplo para {produto}"


CUSTOM_TOOLS = {
    "consultar_catalogo": consultar_catalogo,
}
```

Depois inclua o nome da tool em `src/summit_agents/agents/factory.py`.

## Adicionar um agente especialista

1. Crie `prompts/meu_especialista.md`.
2. Adicione uma função `build_meu_especialista()` em `src/summit_agents/agents/factory.py`.
3. Registre o agente no `build_agent()`.
4. Inclua o especialista em `handoffs` do roteador ou como `agent.as_tool(...)`, dependendo do
   ownership desejado para a resposta final.

## Adicionar MCP

Use `src/summit_agents/integrations/mcp.py` para helpers de MCP hospedado ou local.
MCP hospedado é adequado para servidores remotos públicos. MCP local/privado é melhor quando
o runtime da aplicação deve controlar rede, aprovações e filtragem.

## Evoluir avaliações

Comece com `evals/smoke_cases.jsonl` para capturar perguntas recorrentes da palestra.
Quando o workflow estabilizar, transforme esses casos em datasets e graders na plataforma
OpenAI para medir regressão de prompt, tool use, handoffs e políticas.
