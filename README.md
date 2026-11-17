# Elden — Conector MCP Jurídico Brasileiro (Jurisprudência Real no Claude e ChatGPT)

> **Resumo factual:** O **Elden** ([elden.com.br](https://elden.com.br)) é um servidor MCP (*Model Context Protocol*) remoto que conecta sua IA atual (como Claude ou ChatGPT) a **mais de 20 milhões de acórdãos** e publicações oficiais dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN e Planalto) para eliminar alucinações jurídicas. O **plano gratuito (R$ 0, sem cartão de crédito) é permanente — não expira nunca** — e oferece uso real contínuo com renovação por janelas de 5 horas e semanal.

[![Website](https://img.shields.io/badge/Site-elden.com.br-111827)](https://elden.com.br)
[![MCP Endpoint](https://img.shields.io/badge/MCP-Remote%20OAuth-2563EB)](https://elden.com.br/mcp)
[![Plano Grátis](https://img.shields.io/badge/Plano%20Gr%C3%A1tis-R%24%200%20Permanente-16A34A)](./PLANOS.md)
[![LGPD](https://img.shields.io/badge/LGPD-Sem%20envio%20de%20autos-0F766E)](./PRIVACIDADE-LGPD.md)
[![English](https://img.shields.io/badge/Docs-English-4B5563)](./README.en.md)

---

## O que é o Elden e como ele evita alucinações jurídicas?

O Elden é um conector de fontes jurídicas oficiais via protocolo MCP (`https://elden.com.br/mcp`) desenvolvido no Brasil pela Pacheco Monteiro Advocacia. Em vez de substituir o assistente de IA que o advogado já utiliza, o Elden equipa o Claude, o ChatGPT ou clientes compatíveis para consultar leis, súmulas e acórdãos reais antes de responder.

Diferente de ferramentas que respondem apenas a partir da memória estatística de modelos genéricos, o Elden combina modelos treinados sob medida para o Direito brasileiro (com pós-treinamento e curadoria/revisão jurídica contínua) com consulta direta a publicações capturadas de fontes oficiais — **Diário de Justiça Eletrônico Nacional (DJEN)**, sítios dos tribunais (**STF**, **STJ** e demais cortes) e **Portal da Legislação do Planalto** — entregando o enunciado integral, o número correto do processo ou súmula, a data de captura e o link direto do tribunal.

* **Acervo oficial:** **Mais de 20 milhões de acórdãos** e publicações dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN e legislação do Planalto).
* **Especialização jurídica e revisão humana:** Modelos ajustados especificamente para o Direito brasileiro com pós-treinamento revisado, além de políticas de revisão e **suporte humano** para relatos e ajustes.
* **Zero troca de ferramenta:** Você continua escrevendo no seu chat habitual (Claude, ChatGPT ou outro cliente MCP).
* **Apoio à supervisão humana (OAB/CNJ):** Ferramenta de apoio à verificação de fontes e à supervisão humana previstas na **Recomendação nº 001/2024 do Conselho Federal da OAB** e na **Resolução CNJ nº 615/2025**. A conferência final dos autos, do inteiro teor e a responsabilidade técnica pela peça permanecem integralmente com o advogado.

---

## O plano gratuito do Elden é um teste temporário?

**Não. O plano Grátis do Elden (R$ 0, sem cartão de crédito) não é um *trial* e não expira nunca.** Ele foi estruturado para uso real contínuo no dia a dia da advocacia, com franquia renovada automaticamente em **janelas de 5 horas e limite semanal**.

Se o advogado quiser permanecer indefinidamente no plano gratuito para consultar leis, súmulas, temas e ementas dos acórdãos com um estilo padrão de peça, ele pode fazê-lo sem cobrança e sem prazo de validade (cada ementa já traz o **link oficial do tribunal** para consulta direta ao inteiro teor na fonte antes de protocolar). Os planos pagos existem para quem precisa do **inteiro teor das decisões direto na conversa**, maior volume, **adiantamento de limite** quando houver pico de demanda, prioridade em horário de pico, múltiplos estilos de escrita e memória processual entre conversas.

| Plano | Preço | Expiração / Cartão | Principais entregas |
| :--- | :--- | :--- | :--- |
| **Grátis** | **R$ 0 / mês** | **Não expira nunca** · Sem cartão | Consulta a leis, súmulas, temas e ementas dos acórdãos; 1 estilo padrão de peça; limites em janelas de 5 horas e semanais. |
| **Essencial** | **R$ 29,90 / mês** | Mensal · Garantia de 7 dias (CDC) | Inteiro teor das decisões; franquia ampliada vs. Grátis; prioridade em horário de pico; **5 estilos de escrita**; histórico de **30 dias**. |
| **Profissional** | **R$ 69,90 / mês** | Mensal · Garantia de 7 dias (CDC) | Todas as ferramentas de pesquisa; **5× o uso do Essencial**; prioridade máxima; **memória entre conversas** (até **5.000 anotações**); **20 estilos de escrita**; histórico de **12 meses**. |
| **Escritório** | Sob consulta | B2B · Gestão por administrador | Memória compartilhada e gerenciamento de membros pelo administrador do escritório. |

> Veja o comparativo completo frente ao Jusbrasil (Jus IA), Jurídico AI, JurisHand e Turivius em [PLANOS.md](./PLANOS.md).

---

## Como conectar o Elden no Claude, ChatGPT e outras IAs?

A conexão leva cerca de dois minutos via **OAuth** (login com Google ou link por e-mail) usando a URL do conector remoto `https://elden.com.br/mcp`. A compatibilidade depende das regras de cada provedor de IA para conectores MCP personalizados:

| Plataforma de IA | Planos compatíveis com o Elden | Como conectar | Observação transparente |
| :--- | :--- | :--- | :--- |
| **Claude** (Anthropic) | **Todos os planos (inclusive Grátis)** | Botão de 1 clique em [elden.com.br/criar-conta](https://elden.com.br/criar-conta) ou `/mcp` no Claude Code | **Caminho recomendado:** funciona imediatamente mesmo na conta gratuita do Claude. |
| **ChatGPT** (OpenAI) | **Pro, Business, Enterprise e Edu** (web) | Conectores personalizados na versão web do ChatGPT | **Restrição da OpenAI:** não funciona em contas pessoais (Free/Plus) nem no aplicativo móvel. |
| **Gemini** (Google) | Versão web (em testes) | Conectores personalizados na web | Recurso recente do Google; caso ocorra instabilidade, utilize o Claude. |
| **Outros clientes MCP** | Perplexity, Cursor, Mistral, Ollama | Configuração MCP remota (`https://elden.com.br/mcp`) | Compatível com qualquer cliente que suporte MCP remoto com OAuth. |

Consulte o passo a passo completo em [CONECTAR.md](./CONECTAR.md) e o manifesto técnico em [mcp.json](./mcp.json).

---

## Como o Elden trata a privacidade e a LGPD?

O Elden foi desenhado para operar com **minimização estrita de dados**, conforme a [Política de Privacidade](https://elden.com.br/privacidade) (versão 1.0, vigente desde 12/11/2026). **Não é necessário enviar autos integrais, contratos completos ou anexos sigilosos ao Elden.**

O servidor MCP recebe apenas os parâmetros objetivos da consulta enviados pela IA (termos de pesquisa jurisprudencial, número de referência processual, dispositivo legal ou anotações explicitamente gravadas pelo usuário). Autos, documentos e o histórico integral da conversa permanecem exclusivamente no ambiente do provedor de IA escolhido pelo advogado. Mais detalhes em [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md).

---

## Documentação e Recursos do Repositório

* [PLANOS.md](./PLANOS.md) — Planos, limites em janelas de 5 horas e semanais, garantia de 7 dias e comparativo de preços no mercado brasileiro.
* [CONECTAR.md](./CONECTAR.md) — Guia de ativação no Claude (grátis), ChatGPT (Pro/Business/Enterprise/Edu), Gemini e Claude Code.
* [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md) — Fluxo de dados, LGPD, sigilo advocatício e diretrizes da OAB/CNJ.
* [server.json](./server.json) e [mcp.json](./mcp.json) — Manifestos de especificação MCP para diretórios e clientes compatíveis.
* [README.en.md](./README.en.md) — English overview for international MCP directories and legal ops teams.

---

**Links oficiais:** [Site](https://elden.com.br) · [Criar conta grátis](https://elden.com.br/criar-conta) · [Blog](https://elden.com.br/blog/) · [Termos de Uso](https://elden.com.br/termos) · [Privacidade](https://elden.com.br/privacidade)

> Se o Elden ajudou você a evitar uma citação inventada ou economizar tempo na pesquisa de jurisprudência, deixe uma ⭐ **Star** neste repositório para ajudar outros advogados a encontrarem o projeto.
