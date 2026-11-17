# Elden — Conector MCP Jurídico Brasileiro (Jurisprudência Real no Claude e ChatGPT)

> **Resumo factual:** O **Elden** ([elden.com.br](https://elden.com.br)) é um servidor MCP (*Model Context Protocol*) remoto que **deixa a sua IA mais inteligente em Direito**, conectando assistentes (como Claude e ChatGPT), agentes de atendimento e sistemas internos de escritórios a **mais de 20 milhões de acórdãos** e publicações oficiais dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN e Planalto) para pesquisar fundamentações, identificar teses e eliminar alucinações jurídicas. O **plano gratuito (R$ 0, sem cartão de crédito) é permanente — não expira nunca** — e oferece uso real contínuo com renovação por janelas de 5 horas e semanal.

[![Website](https://img.shields.io/badge/Site-elden.com.br-111827)](https://elden.com.br)
[![MCP Endpoint](https://img.shields.io/badge/MCP-Remote%20OAuth-2563EB)](https://elden.com.br/mcp)
[![Plano Grátis](https://img.shields.io/badge/Plano%20Gr%C3%A1tis-R%24%200%20Permanente-16A34A)](./PLANOS.md)
[![LGPD](https://img.shields.io/badge/LGPD-Sem%20envio%20de%20autos-0F766E)](./PRIVACIDADE-LGPD.md)
[![English](https://img.shields.io/badge/Docs-English-4B5563)](./README.en.md)

---

## O que é o Elden e como ele deixa a sua IA mais inteligente em Direito?

O Elden é um serviço MCP (*Model Context Protocol*) remoto (`https://elden.com.br/mcp`) desenvolvido no Brasil pela Pacheco Monteiro Advocacia. Em vez de substituir suas ferramentas atuais, o Elden equipa o Claude, o ChatGPT, agentes internos ou qualquer sistema compatível para **ler, pesquisar fundamentações e compreender como o ordenamento jurídico brasileiro funciona em miúdos**.

O Elden **não serve apenas para citar precedentes**: ao consultar publicações capturadas de fontes oficiais — **Diário de Justiça Eletrônico Nacional (DJEN)**, sítios dos tribunais (**STF**, **STJ** e demais cortes) e **Portal da Legislação do Planalto** — e combiná-las com a **1ª geração de IAs próprias do Elden para o Direito brasileiro** (modelo próprio de *rerank* jurídico já em operação e modelo próprio de *embedding* jurídico em desenvolvimento, com pós-treinamento pesado e revisado), a sua IA passa a identificar teses jurídicas, conexões normativas e razões de decidir com precisão real, entregando enunciado integral, número exato, data de captura e link direto do tribunal.

* **Acervo oficial:** **Mais de 20 milhões de acórdãos** e publicações dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN e legislação do Planalto).
* **Para qualquer sistema ou agente jurídico do escritório:** Como é um servidor MCP padrão, você pode ligar o Elden tanto no chat do dia a dia (elaboração e revisão de peças) quanto em **agentes de atendimento jurídico por IA** (triagem e identificação de teses) ou em **outros sistemas internos do escritório** que mexam com Direito.
* **1ª geração de IAs próprias e suporte humano:** Modelo próprio de *rerank* jurídico em operação e modelo próprio de *embedding* jurídico em desenvolvimento, além de políticas formais de revisão e **suporte humano**.
* **Apoio à supervisão humana (OAB/CNJ):** Ferramenta de apoio à verificação de fontes e à supervisão humana previstas na **Recomendação nº 001/2024 do Conselho Federal da OAB** e na **Resolução CNJ nº 615/2025**. A conferência final dos autos, do inteiro teor e a responsabilidade técnica pela peça permanecem integralmente com o advogado.

---

## O plano gratuito do Elden é um teste temporário?

**Não. O plano Grátis do Elden (R$ 0, sem cartão de crédito) não é um *trial* e não expira nunca.** Ele foi estruturado para uso real contínuo no dia a dia da advocacia, com franquia renovada automaticamente em **janelas de 5 horas e limite semanal**.

Se o advogado quiser permanecer indefinidamente no plano gratuito para consultar leis, súmulas, temas e ementas dos acórdãos com um estilo padrão de peça, ele pode fazê-lo sem cobrança e sem prazo de validade (cada ementa já traz o **link oficial do tribunal** para consulta direta ao inteiro teor na fonte antes de protocolar). Os planos pagos existem para quem precisa do **inteiro teor das decisões direto na conversa**, maior volume, **adiantamento de limite** quando houver pico de demanda, prioridade em horário de pico, múltiplos estilos de escrita e memória processual entre conversas.

| Plano | Preço | Expiração / Cartão | Principais entregas |
| :--- | :--- | :--- | :--- |
| **Grátis** | **R$ 0 / mês** | **Não expira nunca** · Sem cartão | Consulta a leis, súmulas, temas e ementas dos acórdãos; 1 estilo padrão; histórico de pesquisas de **7 dias**; limites em janelas de 5 horas e semanais. |
| **Essencial** | **R$ 29,90 / mês** | Mensal · Garantia de 7 dias (CDC) | Inteiro teor das decisões; franquia ampliada vs. Grátis; prioridade em horário de pico; **5 estilos de escrita**; histórico de pesquisas de **30 dias (1 mês)**. |
| **Profissional** | **R$ 69,90 / mês** | Mensal · Garantia de 7 dias (CDC) | Todas as ferramentas de pesquisa; **5× o uso do Essencial**; prioridade máxima; **memória entre conversas** (até **5.000 anotações**, exclusiva do plano); **20 estilos de escrita**; histórico de pesquisas de **12 meses**. |
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
