# Elden — Conector MCP Jurídico Brasileiro (Jurisprudência Real no Claude e ChatGPT)

> **Resumo factual:** O **Elden** ([elden.com.br](https://elden.com.br)) é um servidor MCP (*Model Context Protocol*) remoto que **deixa a sua IA mais inteligente em Direito**, conectando assistentes (como Claude e ChatGPT), agentes de atendimento e sistemas internos de escritórios a **mais de 20 milhões de acórdãos** e publicações oficiais dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN e Planalto) para pesquisar fundamentações, identificar teses e eliminar alucinações jurídicas. O **plano gratuito (R$ 0, sem cartão de crédito) é permanente — não expira nunca** — e oferece uso real contínuo com renovação por janelas de 5 horas e semanal.

[![Website](https://img.shields.io/badge/Site-elden.com.br-111827)](https://elden.com.br)
[![MCP Endpoint](https://img.shields.io/badge/MCP-Remote%20OAuth-2563EB)](https://elden.com.br/mcp)
[![Plano Grátis](https://img.shields.io/badge/Plano%20Gr%C3%A1tis-R%24%200%20Permanente-16A34A)](./PLANOS.md)
[![Criptografia](https://img.shields.io/badge/Criptografia-TLS%20%2B%20Repouso-0284C7)](./SECURITY.md)
[![LGPD](https://img.shields.io/badge/LGPD-Zero%20Venda%20de%20Dados-0F766E)](./PRIVACIDADE-LGPD.md)
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

Se o advogado quiser permanecer indefinidamente no plano gratuito para consultar leis, súmulas, temas e ementas dos acórdãos (até 3 resultados por busca e degustação de 2 usos de `buscar_fundamentacao` a cada 5 horas) usando o estilo forense padrão de peça, ele pode fazê-lo sem cobrança e sem prazo de validade (cada ementa já traz o **link oficial do tribunal** para consulta direta ao inteiro teor na fonte antes de protocolar). Os planos pagos existem para quem precisa do **inteiro teor das decisões e conferência literal de citações (`conferir_transcricao`, `dossie_precedente`, `pesquisar_questao`)**, **criação e edição de estilos próprios de escrita**, **busca profunda (8 a 15 resultados por eixo)**, **adiantamento de limite** em picos de demanda e **memória processual entre conversas**.

| Plano | Preço | Expiração / Cartão | Principais entregas |
| :--- | :--- | :--- | :--- |
| **Grátis** | **R$ 0 / mês** | **Não expira nunca** · Sem cartão | Até **3 resultados por busca**; degustação de **`buscar_fundamentacao` (2 usos / 5h)**; estilo forense padrão (somente leitura); histórico de **7 dias**; janelas de 5h e semanais (a própria IA avisa ao bater o limite). |
| **Essencial** | **R$ 29,90 / mês** | Mensal · Garantia de 7 dias (CDC) | **`buscar_fundamentacao` liberado**, `dossie_precedente`, `pesquisar_questao` e `conferir_transcricao`; até **8 resultados/busca**; adiantamento de limite; **5 estilos de escrita próprios** (criar/editar, inclusive a partir de PDF seu); **memória entre conversas (até 100 anotações)**; histórico de **30 dias**. |
| **Profissional** | **R$ 69,90 / mês** | Mensal · Garantia de 7 dias (CDC) | Todas as ferramentas sem trava e até **15 resultados/busca**; **5× o uso do Essencial**; adiantamento de limite e prioridade máxima; **memória ampla (até 5.000 anotações)**; **20 estilos de escrita próprios** (inclusive a partir de PDF seu); histórico de **12 meses**. |
| **Escritório** | Sob consulta | B2B · Gestão por administrador | Memória compartilhada (até 20.000 anotações), até 50 estilos da banca e gerenciamento de membros pelo administrador. |

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

## Segurança, Criptografia e Privacidade (LGPD e Sigilo Profissional)

O Elden foi projetado para que **advogados e escritórios possam utilizar a plataforma sem medo**, unindo minimização estrita de dados, criptografia e compromisso absoluto de confidencialidade ([Política de Privacidade v1.0](https://elden.com.br/privacidade)):

* **Criptografia em trânsito e em repouso:** toda comunicação com `https://elden.com.br/mcp` usa **HTTPS/TLS** com proteção de borda; anotações de memória contextual são armazenadas **de forma cifrada e isoladas por conta**; chaves de API e tokens OAuth/sessão ficam protegidos por **hash irreversível** (nunca em texto puro), com **revogação em tempo real** no painel; backups são cifrados e logs operacionais omitem credenciais e conteúdos de consultas.
* **Recomendamos não enviar dados sensíveis:** **não é necessário enviar autos integrais, contratos, nomes de partes, CPF/RG ou anexos sigilosos** ao Elden. O servidor recebe apenas os parâmetros objetivos da pesquisa enviados pela IA — formule as consultas em **tese jurídica**, mantendo autos e documentos exclusivamente no provedor de IA de sua escolha.
* **Zero comercialização de dados (mesmo que algo sensível seja enviado):** mesmo que um usuário acabe incluindo alguma informação sensível em uma busca ou anotação, **nós nunca vendemos, alugamos, cedemos para publicidade ou comercializamos nenhum dado**. Suas memórias e preferências são isoladas por conta, sem rastreadores publicitários, e podem ser apagadas diretamente por você a qualquer momento.

Mais detalhes técnicos e regulatórios (OAB / CNJ / LGPD) em [SECURITY.md](./SECURITY.md) e [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md).

---

## Documentação e Recursos do Repositório

* [PLANOS.md](./PLANOS.md) — Planos, limites em janelas de 5 horas e semanais, garantia de 7 dias e comparativo de preços no mercado brasileiro.
* [CONECTAR.md](./CONECTAR.md) — Guia de ativação no Claude (grátis), ChatGPT (Pro/Business/Enterprise/Edu), Gemini e Claude Code.
* [SECURITY.md](./SECURITY.md) — Controles técnicos de segurança, criptografia, OAuth e canal para relato de vulnerabilidades.
* [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md) — Fluxo de dados, zero comercialização, LGPD, sigilo advocatício e diretrizes da OAB/CNJ.
* [CHANGELOG.md](./CHANGELOG.md) — Histórico público de atualizações do acervo, modelos próprios e integrações.
* [server.json](./server.json) e [mcp.json](./mcp.json) — Manifestos de especificação MCP para diretórios e clientes compatíveis.
* [README.en.md](./README.en.md) — English overview for international MCP directories and legal ops teams.

---

## Guias, Benchmark e Artigos Oficiais (`elden.com.br`)

Recursos públicos curados para avaliar o conector MCP do Elden, comparar planos e consultar guias técnicos e regulatórios sobre IA jurídica no Brasil:

* **Páginas principais:** [Planos e Preços](https://elden.com.br/planos) · [Benchmark Jurídico (IA sem alucinações)](https://elden.com.br/benchmark) · [Blog Técnico e Jurídico](https://elden.com.br/blog/)
* **Artigos publicados:**
  * [Famílias de IA em novembro de 2026: mapa técnico completo por provedor e projeções para a advocacia](https://elden.com.br/blog/familias-de-modelos-ia-novembro-2026/)
  * [Qwen 4 chegou: o que muda na IA jurídica e o que esperar dos próximos anos](https://elden.com.br/blog/qwen-4-e-futuras-projecoes-ia-juridica/)
  * [Melhores modelos de IA para advocacia em novembro de 2026: Gemini 4, Muse Wonder, Claude 5.5, GPT-6, Kimi e DeepSeek com dados conferidos](https://elden.com.br/blog/melhores-modelos-ia-para-advocacia-2026/)
  * [Elden no GitHub: como funciona o plano gratuito permanente e por que ele não é um teste](https://elden.com.br/blog/elden-no-github-e-plano-gratis-permanente/)
  * [Além de citar acórdãos: como conectar sua IA ao ordenamento jurídico brasileiro](https://elden.com.br/blog/como-deixar-ia-mais-inteligente-em-direito-brasileiro/)
  * [Jurisprudência inventada por IA: o que os tribunais têm decidido](https://elden.com.br/blog/tribunais-e-citacoes-inventadas-por-ia/)
  * [OAB aprova recomendações sobre IA generativa na advocacia](https://elden.com.br/blog/oab-recomendacoes-para-uso-de-ia/)
  * [Resolução CNJ n. 615: IA no Judiciário e advocacia](https://elden.com.br/blog/cnj-resolucao-615-ia-no-judiciario/)

---

**Links oficiais:** [Site](https://elden.com.br) · [Planos](https://elden.com.br/planos) · [Benchmark](https://elden.com.br/benchmark) · [Criar conta grátis](https://elden.com.br/criar-conta) · [Blog](https://elden.com.br/blog/) · [Termos de Uso](https://elden.com.br/termos) · [Privacidade](https://elden.com.br/privacidade)

> Se o Elden ajudou você a evitar uma citação inventada ou economizar tempo na pesquisa de jurisprudência, deixe uma ⭐ **Star** neste repositório para ajudar outros advogados a encontrarem o projeto.
