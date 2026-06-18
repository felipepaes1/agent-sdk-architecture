# Summit Agents SDK Starter

Template Python plug-and-play para participantes de uma palestra sobre OpenAI Agents SDK.
Ele foi organizado para que qualquer pessoa possa clonar, trocar prompts, adicionar tools,
conectar integrações e evoluir para workflows multiagente sem reestruturar o projeto.

## O que vem pronto

- `prompts/`: instruções editáveis em Markdown.
- `src/summit_agents/agents/`: factory dos agentes e roteador.
- `src/summit_agents/tools/`: tools Python com `@function_tool` e registry simples.
- `src/summit_agents/integrations/`: helpers para sessão local e MCP.
- `src/summit_agents/workflows/`: execução de uma rodada com tracing opcional.
- `evals/`: casos de fumaça para comparar comportamento ao mudar prompts e tools.
- `docs/`: guia de arquitetura e pontos de extensão.
- `tests/`: teste pequeno para validar o loader de prompts.

Veja também `docs/prompt-templates.md` para prompts copiáveis que ajudam a adaptar este
starter para outros domínios, tools e workflows.

## Setup rápido

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Git Bash no Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

Bash no Linux, macOS ou WSL:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cp .env.example .env
```

Edite `.env` e configure `OPENAI_API_KEY`.

## Rodar

```bash
summit-agent doctor
summit-agent ask "Explique em 3 bullets quando usar Agents SDK."
summit-agent ask --agent assistant "Como adiciono uma nova tool?"
summit-agent ask --session demo-001 "Lembre que minha palestra é sobre SDK de agents."
```

Por padrão o template usa `OPENAI_MODEL=gpt-5.5`, alinhado com a documentação atual da
OpenAI no momento da criação deste scaffold. Troque no `.env` quando quiser comparar modelos.

## Como customizar

1. Troque o texto em `prompts/assistant.md`, `prompts/researcher.md` ou `prompts/router.md`.
2. Crie uma função em `src/summit_agents/tools/custom.py`, decore com `@function_tool` e registre em `CUSTOM_TOOLS`.
3. Adicione MCP remoto ou local em `src/summit_agents/integrations/mcp.py`.
4. Ajuste a composição em `src/summit_agents/agents/factory.py`.
5. Adicione exemplos em `evals/smoke_cases.jsonl` para medir regressão de comportamento.
6. Rode `python -m compileall src tests` e depois teste com `summit-agent ask`.

## Referências oficiais

- Agents SDK: https://developers.openai.com/api/docs/guides/agents
- Quickstart: https://developers.openai.com/api/docs/guides/agents/quickstart
- Agent definitions: https://developers.openai.com/api/docs/guides/agents/define-agents
- Running agents: https://developers.openai.com/api/docs/guides/agents/running-agents
- Orchestration and handoffs: https://developers.openai.com/api/docs/guides/agents/orchestration
- Integrations and observability: https://developers.openai.com/api/docs/guides/agents/integrations-observability
