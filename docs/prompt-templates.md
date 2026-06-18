# Prompts para adaptar este starter

Use estes prompts no Codex ou em outro harness de programação assistida para transformar este
starter em um projeto mais próximo do seu caso real. Copie um bloco, substitua os campos entre
colchetes e rode a partir da raiz do repositório.

Os prompts assumem que o assistente pode ler e editar o projeto. Quando quiser mais controle,
adicione a frase: "Antes de editar arquivos, me mostre um plano curto e aguarde minha aprovação."

## 1. Adaptação completa do projeto

```text
Analise todo este projeto e a arquitetura de Agents SDK antes de editar qualquer arquivo.

Quero transformar este starter em um sistema de agentes para:
[INSIRA AQUI O OBJETIVO PRINCIPAL DO SISTEMA]

Contexto do domínio:
[DESCREVA O PÚBLICO, EMPRESA, ÁREA, DADOS DISPONÍVEIS, LIMITAÇÕES E TOM DE RESPOSTA]

O workflow esperado deve:
- [ETAPA 1 DO FLUXO]
- [ETAPA 2 DO FLUXO]
- [ETAPA 3 DO FLUXO]

O agente precisa conseguir:
- [CAPACIDADE OU TOOL 1]
- [CAPACIDADE OU TOOL 2]
- [CAPACIDADE OU TOOL 3]

Funções externas, APIs, bancos, MCPs ou sistemas que talvez sejam necessários:
- [NOME DO SISTEMA] - [O QUE DEVE CONSULTAR OU EXECUTAR]
- [NOME DO SISTEMA] - [O QUE DEVE CONSULTAR OU EXECUTAR]

Regras importantes:
- Mantenha a estrutura plug-and-play do projeto.
- Prefira editar prompts em Markdown quando a mudança for comportamental.
- Crie ou adapte tools em Python quando o agente precisar executar uma ação concreta.
- Atualize os testes ou evals quando o comportamento principal mudar.
- Atualize o README e docs se os comandos ou o fluxo de uso mudarem.

Depois de analisar, implemente a adaptação mínima e funcional para esse caso.
```

## 2. Trocar apenas o comportamento do agente principal

```text
Analise os prompts e a factory de agentes deste projeto.

Quero manter a arquitetura atual, mas trocar o comportamento do agente principal para:
[DESCREVA O NOVO PAPEL DO AGENTE]

O agente deve sempre:
- [REGRA DE COMPORTAMENTO 1]
- [REGRA DE COMPORTAMENTO 2]
- [REGRA DE COMPORTAMENTO 3]

O agente nunca deve:
- [LIMITE OU PROIBIÇÃO 1]
- [LIMITE OU PROIBIÇÃO 2]

Formato de resposta esperado:
[EXEMPLO OU DESCRIÇÃO DO FORMATO]

Edite principalmente os arquivos em `prompts/`. Só altere código se for realmente necessário.
Ao final, indique quais prompts foram alterados e como testar com `summit-agent ask`.
```

## 3. Criar um agente especialista

```text
Analise a arquitetura em `docs/architecture.md`, os prompts existentes e
`src/summit_agents/agents/factory.py`.

Quero adicionar um agente especialista chamado:
[NOME DO ESPECIALISTA]

Responsabilidade desse especialista:
[DESCREVA O QUE ELE RESOLVE MELHOR QUE O AGENTE PRINCIPAL]

Ele deve receber casos quando:
- [CRITÉRIO DE ROTEAMENTO 1]
- [CRITÉRIO DE ROTEAMENTO 2]

Ele deve usar estas tools, se existirem ou forem criadas:
- [TOOL 1]
- [TOOL 2]

Implemente o especialista mantendo o padrão do projeto:
- Crie o prompt Markdown em `prompts/`.
- Adicione a função de build na factory.
- Conecte o especialista ao roteamento, handoff ou `as_tool`, escolhendo a opção mais simples
  para este caso.
- Atualize ou crie um exemplo de avaliação em `evals/`.
```

## 4. Adicionar uma tool Python

```text
Analise `src/summit_agents/tools/` e como as tools são registradas nos agentes.

Quero adicionar uma tool chamada:
[NOME_DA_TOOL]

Objetivo da tool:
[O QUE ELA DEVE FAZER]

Entradas esperadas:
- [PARÂMETRO 1]: [TIPO E DESCRIÇÃO]
- [PARÂMETRO 2]: [TIPO E DESCRIÇÃO]

Saída esperada:
[DESCREVA O RETORNO IDEAL]

Implementação inicial:
- Se depender de API externa, crie primeiro uma versão simulada ou isolada por função helper.
- Use docstring clara, porque ela orienta o uso da tool pelo agente.
- Registre a tool em `CUSTOM_TOOLS`.
- Conecte a tool ao agente certo.
- Adicione um teste simples quando fizer sentido.

Ao final, mostre um comando `summit-agent ask` que force o uso dessa tool.
```

## 5. Conectar uma API externa ou sistema interno

```text
Analise este projeto e proponha a forma mais simples de conectar o sistema abaixo ao workflow
de agentes.

Sistema externo:
[NOME DA API, BANCO, CRM, ERP, PLANILHA, MCP OU SERVIÇO]

O agente precisa:
- [CONSULTAR / CRIAR / ATUALIZAR / VALIDAR ALGO]
- [DESCREVA AS OPERAÇÕES PRINCIPAIS]

Dados de configuração:
- Variáveis de ambiente necessárias: [LISTA]
- Credenciais não devem ser hardcoded.
- `.env.example` deve ser atualizado se novas variáveis forem criadas.

Implemente:
- Um helper de integração em `src/summit_agents/integrations/` se houver código reutilizável.
- Uma ou mais tools em `src/summit_agents/tools/`.
- Tratamento simples de erro para falhas de rede, credenciais ausentes ou resposta inesperada.
- Documentação curta no README ou em `docs/`.
```

## 6. Desenhar um workflow multiagente

```text
Analise o projeto atual e desenhe um workflow multiagente para este caso:
[DESCREVA O CASO DE USO]

Agentes desejados:
- [AGENTE 1]: [RESPONSABILIDADE]
- [AGENTE 2]: [RESPONSABILIDADE]
- [AGENTE 3]: [RESPONSABILIDADE]

O workflow deve seguir esta ordem ou regra:
[DESCREVA SE É SEQUENCIAL, COM ROTEADOR, HANDOFF, AGENTE COMO TOOL, REVISOR ETC.]

Critérios de sucesso:
- [CRITÉRIO 1]
- [CRITÉRIO 2]

Implemente a menor versão funcional:
- Prompts separados para cada agente.
- Factory atualizada.
- Workflow em `src/summit_agents/workflows/` se a execução padrão não for suficiente.
- Exemplos em `evals/` para cobrir pelo menos um caminho feliz e um caso limite.
```

## 7. Criar evals para o caso de uso

```text
Analise os prompts, tools e workflows deste projeto.

Quero criar ou melhorar avaliações para medir se o agente está bom em:
[DESCREVA O COMPORTAMENTO QUE DEVE SER MEDIDO]

Casos obrigatórios:
- Pergunta simples: [EXEMPLO]
- Caso com tool: [EXEMPLO]
- Caso ambíguo: [EXEMPLO]
- Caso que deve recusar ou pedir esclarecimento: [EXEMPLO]

Implemente exemplos em `evals/` no formato já usado pelo projeto.
Se fizer sentido, adicione um teste local pequeno para validar carregamento ou estrutura dos
casos.
```

## 8. Revisar arquitetura antes de uma demo

```text
Faça uma revisão técnica deste projeto pensando em uma demo ao vivo.

Procure por:
- Instruções desatualizadas no README.
- Prompts confusos ou contraditórios.
- Tools registradas mas não conectadas.
- Variáveis de ambiente faltando em `.env.example`.
- Casos simples que deveriam estar cobertos em `evals/` ou testes.
- Erros prováveis ao rodar `summit-agent doctor` e `summit-agent ask`.

Priorize problemas que podem quebrar a demo ou confundir o público.
Depois implemente correções pequenas e seguras.
```

## 9. Transformar um briefing em prompts do projeto

```text
Leia o briefing abaixo e transforme em prompts de agente para este starter.

Briefing:
[COLE AQUI O TEXTO DO CLIENTE, ÁREA OU PROJETO]

Objetivo:
[O QUE O AGENTE DEVE ENTREGAR]

Tom e estilo:
[EXEMPLOS DE TOM, NÍVEL DE FORMALIDADE, IDIOMA, FORMATO]

Regras de negócio:
- [REGRA 1]
- [REGRA 2]
- [REGRA 3]

Saídas esperadas:
- [TIPO DE RESPOSTA 1]
- [TIPO DE RESPOSTA 2]

Edite os prompts em `prompts/` e ajuste a factory apenas se precisar de novos agentes.
Preserve a estrutura do projeto e adicione exemplos em `evals/` que representem o briefing.
```

## 10. Adaptar para workshop ou turma

```text
Analise este starter e adapte o conteúdo para um workshop sobre:
[TEMA DO WORKSHOP]

Público:
[NÍVEL TÉCNICO, ÁREA, IDIOMA, TEMPO DISPONÍVEL]

Quero que os participantes consigam:
- [APRENDIZADO 1]
- [APRENDIZADO 2]
- [APRENDIZADO 3]

Adapte:
- README com instruções claras para esse público.
- Prompts para refletir exemplos do tema.
- Tools de exemplo simples e fáceis de entender.
- Evals com perguntas que os participantes fariam.

Evite complexidade desnecessária. O projeto deve continuar fácil de clonar, rodar e modificar.
```
