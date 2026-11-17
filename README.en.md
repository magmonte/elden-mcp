# Elden — Brazilian Legal MCP Server (Verified Case Law & Legislation for Claude and ChatGPT)

> **Summary:** **Elden** ([elden.com.br](https://elden.com.br)) is a remote Model Context Protocol (MCP) server (`https://elden.com.br/mcp`) that connects your existing AI assistant (Claude, ChatGPT, Cursor, etc.) to **more than 20 million official Brazilian court rulings** (STF, STJ, state and federal courts via DJEN) and federal legislation (Planalto) to eliminate legal hallucinations. Its **Free tier (R$ 0/month, no credit card required) is permanent — it never expires.**

[Versão em Português (README.md)](./README.md)

---

## Why Elden?

Generic LLMs frequently fabricate case numbers, misquote Brazilian Supreme Court (STF) or Superior Court of Justice (STJ) rulings, or rely on outdated statutes. Instead of forcing lawyers to abandon Claude or ChatGPT for an expensive closed platform, Elden plugs directly into their existing chat via **OAuth + Remote MCP**:

- **20M+ Official Court Rulings & Legislation:** Indexed from official sources (DJEN, STF, STJ, and Planalto), returning full statements, exact case numbers, dates, and direct court links.
- **Custom Post-Trained Legal Models:** Models tailored and continuously reviewed for Brazilian law, backed by human review and support policies.
- **Strict Data Minimization (LGPD):** No need to upload full case files or confidential attachments to Elden; only objective search parameters are sent by the AI.
- **Permanent Free Tier:** Not a limited-time trial. Daily quota resets every day at midnight (BRT), with **limit advances** available for demand spikes and paid plans starting at R$ 29.90/month (Essencial) and R$ 69.90/month (Profissional).

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
