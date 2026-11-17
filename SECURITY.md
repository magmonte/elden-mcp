# Política de Segurança (`SECURITY.md`)

A segurança e a confidencialidade no uso jurídico são prioridades arquiteturais do **Elden** ([elden.com.br](https://elden.com.br)). Esta página descreve as proteções técnicas implementadas no servidor MCP remoto (`https://elden.com.br/mcp`) e como reportar eventuais vulnerabilidades.

---

## 1. Controles Técnicos Implementados

### Criptografia em trânsito e em repouso
- **Trânsito (HTTPS / TLS):** toda comunicação entre o cliente de IA (Claude, ChatGPT, Gemini, Cursor etc.) e o endpoint `https://elden.com.br/mcp` ocorre exclusivamente sob HTTPS/TLS moderno com proteção de borda.
- **Repouso (memória contextual):** anotações de memória contextual gravadas pelo usuário são armazenadas **de forma cifrada e isoladas por conta**.
- **Credenciais e tokens:** chaves de acesso e tokens OAuth/sessão são armazenados apenas por **hash irreversível** (nunca em texto puro) e podem ser revogados em tempo real no painel da conta.
- **Cópias de segurança:** backups são gerados e armazenados de forma cifrada.

### Controle de acesso e isolamento
- **OAuth com escopos granulares:** suporte a escopos mínimos (ex.: `factum:read` para consulta somente leitura e `factum:write` apenas quando o usuário autoriza gravação de estilos ou memórias).
- **Isolamento estrito por usuário:** nenhum usuário consegue consultar, alterar ou apagar anotações de memória ou preferências de estilo de outra conta.
- **Proteção contra alterações acidentais e injeção:** criação/exclusão de estilos de redação e sobrescrita/exclusão de memórias exigem confirmação explícita; entradas passam por validação contra padrões de *prompt injection*.
- **Logs operacionais limpos:** registros de telemetria operacional omitem credenciais e conteúdos de consultas.
- **Cookies estritamente necessários:** sem cookies publicitários, de rastreamento ou perfilamento comercial.

---

## 2. Minimização de Dados e Uso Seguro na Advocacia

- **Não envie autos integrais:** o Elden não precisa receber petições completas, contratos ou documentos sigilosos. O ideal é formular consultas em **tese jurídica**, mantendo autos e anexos exclusivamente no ambiente do provedor de IA escolhido pelo advogado.
- **Compromisso absoluto de não comercialização:** mesmo que o usuário acabe incluindo alguma informação sensível em uma busca ou anotação, **o Elden não vende, não aluga, não cede para terceiros de publicidade e não comercializa nenhum dado**. Os dados também não são expostos a outros usuários e podem ser apagados diretamente pelo titular no painel ou via suporte.

---

## 3. Como Reportar uma Vulnerabilidade

Se você identificar qualquer falha de segurança, comportamento inesperado de controle de acesso ou vulnerabilidade em `elden.com.br` ou no conector MCP:

1. **Não divulgue publicamente** antes da análise e correção.
2. Envie os detalhes técnicos (passos para reprodução, impacto estimado e evidências sem expor dados de terceiros) para:
   - **E-mail:** [contato@elden.com.br](mailto:contato@elden.com.br)
   - **Assunto sugerido:** `[SECURITY] Descrição resumida da vulnerabilidade`
3. Analisaremos o relato com prioridade e retornaremos com confirmação de recebimento e andamento da correção.
