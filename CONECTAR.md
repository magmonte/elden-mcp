# Guia de Conexão — Elden MCP (`https://elden.com.br/mcp`)

> **Resumo:** A conexão leva cerca de 2 minutos via OAuth (Google ou link por e-mail). **Caminho recomendado:** use no **Claude** (funciona em qualquer plano, inclusive o gratuito). No **ChatGPT**, conectores MCP personalizados funcionam apenas em contas **Business, Enterprise e Edu na web**.

## 1. Claude (Web e Desktop — Recomendado, funciona no Plano Grátis)
1. Acesse [elden.com.br/criar-conta](https://elden.com.br/criar-conta) e crie sua conta gratuita (sem cartão).
2. Clique no botão de conexão direta com o **Claude** ou adicione o conector remoto `https://elden.com.br/mcp` nas configurações de conectores/integrações do Claude.
3. Autorize via **OAuth** (Google ou e-mail) e pronto: pergunte sobre qualquer súmula, acórdão do STF/STJ ou lei.

## 2. Claude Code / Clientes MCP via Terminal ou JSON
No Claude Code:
```bash
claude mcp add --transport http elden https://elden.com.br/mcp
```
Ou utilize o snippet em [`mcp.json`](./mcp.json):
```json
{
  "mcpServers": {
    "elden": {
      "type": "streamable-http",
      "url": "https://elden.com.br/mcp"
    }
  }
}
```

## 3. ChatGPT (OpenAI) — Atenção às Restrições da OpenAI
- **Planos compatíveis:** **ChatGPT Business, Enterprise e Edu** na **versão web** (plano Pro possui suporte apenas para leitura).
- **Não compatível:** Contas pessoais **Free** e **Plus**, e aplicativo móvel do ChatGPT (limitação da própria OpenAI para conectores MCP personalizados).
- Se você usa ChatGPT Free ou Plus, utilize o **Claude gratuito** com o Elden — não há custo adicional.

## 4. Gemini (Google)
Conectores MCP personalizados na web do Gemini ainda estão em fase de testes pelo Google. Caso enfrente instabilidade, utilize o Claude.
