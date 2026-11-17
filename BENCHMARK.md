# Benchmark Elden — Metodologia e Resultados (06/09/2026)

> **Resumo:** Em teste controlado sem acesso aberto à internet, conectar o Elden elevou o acerto de acórdãos reais do Claude Sonnet 5 de **1/60 para 60/60**, levou a **16/20** em jurisprudência recente de 2026 (contra **0/20** do modelo puro) e elevou a nota na 1ª fase do 46º Exame da OAB de **90% para 96%**.

## Metodologia

- **Data de referência:** 06/09/2026 (com execução parcial de ChatGPT/GPT-5.6 em 05/09/2026).
- **Condição:** Modelos avaliados **com e sem** o conector MCP do Elden, sem navegação livre na web.
- **Correção:** Gabarito definitivo da FGV para o 46º Exame da OAB (maio/2026, 80 questões) e conferência mecânica de existência e veracidade de processos, súmulas e dispositivos no acervo oficial.

## Resultados Comparativos

| Tarefa avaliada | Claude Sonnet 5 (só IA) | Claude Sonnet 5 + Elden | MiniMax M3 grátis (só IA) | MiniMax M3 grátis + Elden |
| :--- | :--- | :--- | :--- | :--- |
| **Achar acórdãos reais** (20 pedidos × 3 acórdãos com nº do processo) | 1 de 60 reais | **60 de 60 reais** (1 inventado) | 0 de 60 reais | **60 de 60 reais** |
| **Jurisprudência de 2026** (20 perguntas pós-corte, jun–set/2026) | 0 de 20 certas | **16 de 20 certas** (0 chutes errados) | 0 de 20 certas | **12 de 20 certas** (1 errada) |
| **Conferir citações** (20 citações, sendo 10 inventadas) | 1 de 20 conferidas certo | **19 de 20 conferidas certo** (0 inventadas aceitas) | 4 de 20 conferidas certo | **14 de 20 conferidas certo** (0 inventadas aceitas) |
| **Dizer súmula e lei certas** (12 pontos) | 10 de 12 | **12 de 12** | 2 de 12 | **12 de 12** |
| **46º Exame da OAB** (1ª fase, maio/2026, 80 questões) | 72/80 (90%) | **77/80 (96%)** | 52/80 | **69/80** |
| **Escrever peça com fonte** (citações reais por peça em 5 processos) | 3,6 por peça | **4,8 por peça** | 4,2 por peça | **5,2 por peça** |

### Execução Parcial — GPT-5.6 (Codex CLI, conta gratuita em 05/09/2026)
Até atingir o limite de uso da conta gratuita, o modelo apresentou os seguintes saltos ao conectar o Elden:
- **Acórdãos reais:** de `9/60` (sem Elden) para `15/15` (com Elden).
- **Súmula e lei certas:** de `11/12` para `12/12`.
- **OAB (questões avaliadas):** de `62/64` para `64/64`.
- **Peças com fonte:** de `2,8` para `4,6` citações reais por peça.

*Fonte oficial:* [elden.com.br/benchmark](https://elden.com.br/benchmark)
