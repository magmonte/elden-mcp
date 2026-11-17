# Política de Segurança (`SECURITY.md`)

A segurança e a confidencialidade no uso jurídico são prioridades do **Elden** ([elden.com.br](https://elden.com.br)). Esta página apresenta os princípios de proteção adotados e o canal oficial para relato de vulnerabilidades.

---

## 1. Compromissos de Segurança e Privacidade

- **Criptografia em trânsito e em repouso:** todas as conexões ao site e ao servidor MCP (`https://elden.com.br/mcp`) utilizam HTTPS/TLS; anotações de memória contextual e cópias de segurança são armazenadas de forma cifrada e isoladas por conta.
- **Proteção de credenciais:** chaves de acesso e tokens de autorização são protegidos por armazenamento irreversível (*hash*) e podem ser revogados pelo usuário em tempo real no painel da conta.
- **Sem necessidade de dados sensíveis:** não é necessário enviar autos integrais, contratos ou dados sensíveis para usar o serviço — basta pesquisar em tese jurídica, mantendo documentos no provedor de IA escolhido.
- **Tratamento e segurança específicos:** tudo o que chega ao serviço recebe tratamento dedicado de segurança, com isolamento estrito entre contas e controle de acesso por usuário.
- **Zero comercialização de dados:** mesmo que alguma informação sensível seja incluída pelo usuário, **o Elden não vende, não aluga e não comercializa nenhum dado**, nem exibe anúncios ou utiliza rastreadores publicitários.

---

## 2. Como Reportar uma Vulnerabilidade

Se você identificar qualquer falha de segurança ou comportamento inesperado em `elden.com.br` ou no conector MCP:

1. **Não divulgue publicamente** antes da análise e correção.
2. Envie os detalhes para **[contato@elden.com.br](mailto:contato@elden.com.br)** com o assunto `[SECURITY] Descrição resumida da vulnerabilidade`.
3. O relato será analisado com prioridade e respondido pelo mesmo canal.
