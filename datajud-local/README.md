# Elden DataJud Local MCP (`stdio`)

Conector MCP leve em **Python puro (sem dependências externas)** para consultar processos específicos e movimentações diretamente na **API Pública do DataJud (CNJ)** a partir da sua própria máquina e com a sua própria chave pública do CNJ.

> **Quando usar este módulo vs. o Elden Remoto (`https://elden.com.br/mcp`)?**
> - **Este MCP local (`datajud-local`)** consulta **andamentos e metadados processuais por número CNJ** diretamente no CNJ (sem passar pelo servidor do Elden).
> - **O servidor remoto [elden.com.br/mcp](https://elden.com.br)** pesquisa **ementas de acórdãos (20M+), súmulas, temas repetitivos e legislação federal (Planalto)** sem alucinações jurídicas.

---

## Como rodar localmente

1. Tenha Python 3.10+ instalado (nenhum `pip install` necessário).
2. Defina a variável `DATAJUD_API_KEY` com a chave pública oficial divulgada no portal do CNJ/DataJud.
3. Adicione no seu cliente MCP (`Claude Desktop`, `Claude Code`, `Cursor`, etc.):

```json
{
  "mcpServers": {
    "elden-datajud-local": {
      "command": "python3",
      "args": ["/CAMINHO/PARA/elden-mcp/datajud-local/elden_datajud_mcp.py"],
      "env": {
        "DATAJUD_API_KEY": "SUA_CHAVE_PUBLICA_DATAJUD"
      }
    }
  }
}
```

### Ferramentas disponíveis
- `consultar_processo_datajud(numero_cnj, tribunal)` — busca classe, órgão julgador, assuntos e últimas movimentações de um número CNJ.
- `buscar_processos_por_classe_assunto(tribunal, classe?, assunto?, limite?)` — pesquisa metadados de processos públicos por classe e/ou assunto.
