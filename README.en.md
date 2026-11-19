# Elden — Brazilian Legal MCP Server (Verified Case Law & Legislation for Claude and ChatGPT)

> **Summary:** **Elden** ([elden.com.br](https://elden.com.br)) is a remote Brazilian Legal Model Context Protocol (MCP) server (`https://elden.com.br/mcp`) for **hallucination-free Brazilian case law and legislation research**, connecting Claude, ChatGPT, Cursor, intake agents, and internal law firm systems to **more than 20 million official Brazilian court rulings** (STF, STJ, state and federal courts via DJEN) and federal statutes (Planalto). **Works immediately without signup** in open read-only mode (up to **1,000 queries/day per IP**, 30/min, 1/s), and also offers a **permanent Free tier (R$ 0/month, no credit card)** with OAuth for custom styles and memory.

[Versão em Português (README.md)](./README.md)

---

## What's New: Elden V1.0 Release

Elden now runs on **Elden V1.0**, a proprietary legal retrieval stack trained specifically for Brazilian case law and federal legislation:

- **58.8% Blind Benchmark Accuracy:** Outperforms `Qwen3-Embedding-4B` (`52.0%`), `pplx-embed-v1-0.6b` (`52.0%`), `Qwen3-Embedding-8B` (`50.5%`), `BAAI/bge-m3` (`46.2%`), `multilingual-e5-large` (`44.4%`), and `Amazon Titan v2` (`42.4%`).
- **Full-Text Rulings & Citation Verification:** Queries real proceedings, full-text court rulings (`STF, STJ, TST, STM, state TJs, federal TRFs & labor TRTs via DJEN`), and Planalto statutes, with literal quote and process verification (`conferir_transcricao`, `dossie_precedente`, `pesquisar_questao`).
- **Continuous Daily Updates & Attorney-Client Privilege:** Automated daily ingestion from DJEN and Planalto; no full case files ever need to be sent.

---

## Why Elden?

Generic LLMs frequently fabricate case numbers or misread Brazilian statutory and case law nuances. Instead of forcing firms into a single closed platform, Elden connects via **OAuth + Remote MCP** to make any AI system genuinely smarter in Brazilian law — not only for citing rulings, but for **reading legal reasoning, understanding how Brazilian law works in detail, and identifying legal theses**:

- **20M+ Official Court Rulings & Legislation:** Indexed from official sources (DJEN, STF, STJ, and Planalto), returning full statements, exact case numbers, dates, and direct court links.
- **Built for Multiple Legal Workflows & Internal Systems:** Use it in daily chat for drafting legal briefs, in **AI legal intake/customer service agents** (to identify viable legal theses), or plug it into **multiple internal law firm systems** via standard MCP.
- **Proprietary Legal AI Stack in Production (`v2.0.0`):** Both our **proprietary Brazilian legal embedding model** and **proprietary legal reranker** now run in production in a 2-stage retrieval pipeline, backed by human review and support policies.
  - **Frozen Benchmark (`50,000` rulings + `12,310` federal statute articles):** **Elden-Model + Reranker** achieves **`58.76%` average MRR@10** (`T1 53.41%` / `R@10 86.08%`, `T2 47.27%`, `Legislation 75.59%` / `R@10 85.07%`), outperforming `Qwen/Qwen3-Embedding-4B` (`52.05%`), `Qwen/Qwen3-Embedding-8B` (`50.47%`), `BAAI/bge-m3` (`46.16%`), and `intfloat/multilingual-e5-large` (`44.36%`).
  - **Full Production Scale (`11M+` court rulings):** **3× top-1 recall** (`0.37% → 1.10%`), **+109% R@10** (`4.03% → 8.42%`) vs. the previous reranked stack, **`43.5 ms` (p50)** initial vector retrieval, **`~1.47 s` (p50)** full 2-stage latency, and **100% database-verifiable citations**.
- **Encryption, No Sensitive Data Required & Dedicated Data Protection (LGPD):** All traffic runs over **HTTPS/TLS**, contextual memories are **encrypted at rest and isolated per user**, and tokens/keys are stored as **irreversible hashes** with real-time revocation. **No sensitive client data or full case files are needed** to use Elden — and everything that reaches the service receives **dedicated security handling**, with **zero sale, rental, or commercialization of user data** (see [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md) and [SECURITY.md](./SECURITY.md)).
- **Permanent Free Tier:** Not a limited-time trial. Usage quotas reset in **5-hour rolling windows and weekly cycles** (with up to 3 results per search, standard read-only briefing style, and 2 uses per 5h of the unified `buscar_fundamentacao` tool; the AI notifies the user upon hitting the cap). Paid plans — **Essencial** (R$ 29.90/month: 5 custom writing styles (including from your PDFs), strategy/verification tools, limit advances, up to 8 results/search, and **100 cross-conversation memory notes**) and **Profissional** (R$ 69.90/month: 5x quota, 20 custom styles (including from your PDFs), up to 15 results/search, and up to **5,000 memory notes**) — unlock full customization and deeper retrieval.

---

## Compatibility

| AI Platform | Supported Plans | Connection |
| :--- | :--- | :--- |
| **Claude** (Anthropic) | **All plans (including Free)** | 1-click OAuth at [elden.com.br/criar-conta](https://elden.com.br/criar-conta) or `claude mcp add --transport http elden https://elden.com.br/mcp` |
| **ChatGPT** (OpenAI) | **Pro, Business, Enterprise & Edu** (web) | Custom connectors on ChatGPT web *(OpenAI restricts custom MCPs on Free/Plus and mobile apps)* |
| **Other MCP Clients** | Perplexity, Cursor, Mistral, Ollama | Remote `streamable-http` MCP at `https://elden.com.br/mcp` (see [`mcp.json`](./mcp.json)) |

---

## Official Pages, Benchmark & Blog Articles (`elden.com.br`)

Curated public links for evaluating Elden's legal MCP server, pricing, hallucination benchmarks, and regulatory guidance in Brazil (Portuguese):

- **Core Pages:** [Plans & Pricing](https://elden.com.br/planos) · [Legal AI Benchmark (Zero-Hallucination Evaluation)](https://elden.com.br/benchmark) · [Elden Legal & Technical Blog](https://elden.com.br/blog/)
- **Published Blog Articles:**
  - [GPT-6.2 Astra and GPT-6.2 Sol: Pricing, Performance, Astra for Law, and Brazilian Legal Practice](https://elden.com.br/blog/gpt-6-2-astra-e-sol-lancamento-advocacia-brasileira/)
  - [Brazilian Case Law MCP for Claude and ChatGPT: Practical Guide for Lawyers](https://elden.com.br/blog/mcp-jurisprudencia-brasileira-para-claude-e-chatgpt/)
  - [How to Verify Court Ruling Citations with AI Without Hallucinations](https://elden.com.br/blog/como-conferir-citacao-de-acordao-com-ia-sem-alucinacao/)
  - [How to Research STJ and STF Case Law in Free Claude with Official Sources](https://elden.com.br/blog/como-pesquisar-jurisprudencia-stj-stf-claude-gratis/)
  - [AI Model Families in November 2026: Technical Map by Provider & Legal Projections](https://elden.com.br/blog/familias-de-modelos-ia-novembro-2026/)
  - [Google Gemini 4 in Legal Practice: Carbon, Hydrogen, Argon & 3.8 Flash](https://elden.com.br/blog/gemini-4-na-advocacia-carbon-hydrogen-argon-flash/)
  - [Anthropic Claude 5 in Legal Practice: Fable 5.2, Opus 5.5, Sonnet 5.5 & Haiku 5.5](https://elden.com.br/blog/claude-5-na-advocacia-fable-opus-sonnet-haiku/)
  - [OpenAI GPT-6 in Legal Practice: Astra, Sol, Terra, Luna & GPT-5.5](https://elden.com.br/blog/gpt-6-na-advocacia-astra-sol-terra-luna/)
  - [Meta Muse in Legal Practice: Wonder, Spark 1.3, Ember & Spark Open 816B](https://elden.com.br/blog/meta-muse-na-advocacia-wonder-spark-ember/)
  - [Asian & Open-Weights AI Models in Legal Practice: DeepSeek V4.1, Kimi K3.1, GLM-5.3 & MiniMax M3](https://elden.com.br/blog/ias-asiaticas-pesos-abertos-advocacia-deepseek-kimi-glm-minimax/)
  - [Qwen 4 Is Here: What Changes in Legal AI and Future Outlook](https://elden.com.br/blog/qwen-4-e-futuras-projecoes-ia-juridica/)
  - [Best AI Models for Legal Practice in November 2026 (Verified Data)](https://elden.com.br/blog/melhores-modelos-ia-para-advocacia-2026/)
  - [Elden on GitHub: How the Permanent Free Tier Works and Why It Is Not a Trial](https://elden.com.br/blog/elden-no-github-e-plano-gratis-permanente/)
  - [Beyond Citing Rulings: Connecting Your AI to Brazilian Law via MCP](https://elden.com.br/blog/como-deixar-ia-mais-inteligente-em-direito-brasileiro/)
  - [AI-Fabricated Case Law: What Brazilian Courts Have Decided](https://elden.com.br/blog/tribunais-e-citacoes-inventadas-por-ia/)
  - [OAB Recommendation No. 001/2024 on Generative AI in Legal Practice](https://elden.com.br/blog/oab-recomendacoes-para-uso-de-ia/)
  - [CNJ Resolution No. 615/2025: AI in the Brazilian Judiciary](https://elden.com.br/blog/cnj-resolucao-615-ia-no-judiciario/)

---

Full Portuguese documentation: [README.md](./README.md) · [PLANOS.md](./PLANOS.md) · [CONECTAR.md](./CONECTAR.md) · [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md).

---

*If Elden helped you catch a fabricated citation or speed up legal research, consider leaving a ⭐ Star on this repository so more lawyers can find it.*
