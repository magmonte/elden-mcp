# Elden — Brazilian Legal MCP Server (Verified Case Law & Legislation for Claude and ChatGPT)

> **Summary:** **Elden** ([elden.com.br](https://elden.com.br)) is a remote Model Context Protocol (MCP) server (`https://elden.com.br/mcp`) that **makes your AI smarter in Brazilian law**, connecting your existing AI assistants (Claude, ChatGPT, Cursor), intake agents, and internal law firm systems to **more than 20 million official Brazilian court rulings** (STF, STJ, state and federal courts via DJEN) and federal legislation (Planalto) to understand legal reasoning, identify theses, and eliminate hallucinations. Its **Free tier (R$ 0/month, no credit card required) is permanent — it never expires.**

[Versão em Português (README.md)](./README.md)

---

## Why Elden?

Generic LLMs frequently fabricate case numbers or misread Brazilian statutory and case law nuances. Instead of forcing firms into a single closed platform, Elden connects via **OAuth + Remote MCP** to make any AI system genuinely smarter in Brazilian law — not only for citing rulings, but for **reading legal reasoning, understanding how Brazilian law works in detail, and identifying legal theses**:

- **20M+ Official Court Rulings & Legislation:** Indexed from official sources (DJEN, STF, STJ, and Planalto), returning full statements, exact case numbers, dates, and direct court links.
- **Built for Multiple Legal Workflows & Internal Systems:** Use it in daily chat for drafting legal briefs, in **AI legal intake/customer service agents** (to identify viable legal theses), or plug it into **multiple internal law firm systems** via standard MCP.
- **1st-Generation Proprietary Legal AI Models:** Heavily post-trained and human-reviewed models built for Brazilian law — already operating a **proprietary legal reranker** with a **proprietary legal embedding model** under active development, backed by human review and support policies.
- **Strict Data Minimization (LGPD):** No need to upload full case files or confidential attachments to Elden; only objective search parameters are sent by the AI.
- **Permanent Free Tier:** Not a limited-time trial. Usage quotas reset in **5-hour rolling windows and weekly cycles** (with up to 3 results per search, standard read-only briefing style, and 2 uses per 5h of the unified `buscar_fundamentacao` tool; the AI notifies the user upon hitting the cap). Paid plans — **Essencial** (R$ 29.90/month: 5 custom writing styles, strategy/verification tools, limit advances, up to 8 results/search, and **100 cross-conversation memory notes**, expandable by **+500 notes for +R$ 9.90/month**) and **Profissional** (R$ 69.90/month: 5x quota, 20 custom styles, up to 15 results/search, and up to **5,000 memory notes**) — unlock full customization and deeper retrieval.

---

## Compatibility

| AI Platform | Supported Plans | Connection |
| :--- | :--- | :--- |
| **Claude** (Anthropic) | **All plans (including Free)** | 1-click OAuth at [elden.com.br/criar-conta](https://elden.com.br/criar-conta) or `claude mcp add --transport http elden https://elden.com.br/mcp` |
| **ChatGPT** (OpenAI) | **Pro, Business, Enterprise & Edu** (web) | Custom connectors on ChatGPT web *(OpenAI restricts custom MCPs on Free/Plus and mobile apps)* |
| **Other MCP Clients** | Perplexity, Cursor, Mistral, Ollama | Remote `streamable-http` MCP at `https://elden.com.br/mcp` (see [`mcp.json`](./mcp.json)) |

---

Full Portuguese documentation: [README.md](./README.md) · [PLANOS.md](./PLANOS.md) · [CONECTAR.md](./CONECTAR.md) · [PRIVACIDADE-LGPD.md](./PRIVACIDADE-LGPD.md).

---

*If Elden helped you catch a fabricated citation or speed up legal research, consider leaving a ⭐ Star on this repository so more lawyers can find it.*
