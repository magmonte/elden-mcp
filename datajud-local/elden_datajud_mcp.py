#!/usr/bin/env python3
"""
Elden DataJud Local MCP (stdio)
-------------------------------
Servidor MCP leve, sem dependências externas (apenas biblioteca padrão do Python),
que roda 100% na máquina do usuário para consultar processos na API pública do
DataJud (CNJ) usando a sua própria chave pública do CNJ.

Uso:
  export DATAJUD_API_KEY="cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
  python3 elden_datajud_mcp.py

Para jurisprudência comentada (20M+ acórdãos, ementas, súmulas e leis sem alucinação),
conecte o servidor MCP remoto do Elden: https://elden.com.br/mcp
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

DATAJUD_BASE = "https://api-publica.datajud.cnj.jus.br"
USER_AGENT = "elden-datajud-local-mcp/1.0 (+https://github.com/magmonte/elden-mcp)"

TRIBUNAL_ALIASES = {
    "stf": "api_publica_stf",
    "stj": "api_publica_stj",
    "tst": "api_publica_tst",
    "tse": "api_publica_tse",
    "stm": "api_publica_stm",
    "trf1": "api_publica_trf1",
    "trf2": "api_publica_trf2",
    "trf3": "api_publica_trf3",
    "trf4": "api_publica_trf4",
    "trf5": "api_publica_trf5",
    "trf6": "api_publica_trf6",
}


def _resolver_indice(tribunal: str) -> str:
    t = re.sub(r"[^a-z0-9]", "", (tribunal or "").strip().lower())
    if not t:
        raise ValueError("Informe a sigla do tribunal (ex.: TJCE, TJSP, TRF1, TRT7, STJ).")
    if t in TRIBUNAL_ALIASES:
        return TRIBUNAL_ALIASES[t]
    if re.fullmatch(r"(tj[a-z]{2}|trt\d{1,2}|tre[a-z]{2}|tjm[a-z]{2})", t):
        return f"api_publica_{t}"
    raise ValueError(f"Tribunal não reconhecido para o DataJud: {tribunal}")


def _datajud_search(indice: str, query: dict, size: int = 5) -> dict:
    api_key = (os.environ.get("DATAJUD_API_KEY") or "").strip()
    if not api_key:
        raise RuntimeError(
            "Variável DATAJUD_API_KEY não configurada. Obtenha a chave pública oficial "
            "no portal DataJud do CNJ e defina DATAJUD_API_KEY no ambiente."
        )
    url = f"{DATAJUD_BASE}/{indice}/_search"
    body = json.dumps({"size": max(1, min(int(size), 10)), "query": query}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"APIKey {api_key}",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        detalhe = e.read().decode("utf-8", "replace")[:300]
        raise RuntimeError(f"DataJud retornou HTTP {e.code}: {detalhe}") from e


def _formatar_hit(src: dict) -> str:
    num = src.get("numeroProcesso", "?")
    classe = (src.get("classe") or {}).get("nome", "?")
    orgao = (src.get("orgaoJulgador") or {}).get("nome", "?")
    grau = src.get("grau", "?")
    ajuiz = src.get("dataAjuizamento", "?")
    atualiz = src.get("dataHoraUltimaAtualizacao", "?")
    assuntos = ", ".join(a.get("nome", "") for a in (src.get("assuntos") or []) if a.get("nome")) or "—"
    movs = src.get("movimentos") or []
    movs_ord = sorted(movs, key=lambda m: m.get("dataHora", ""), reverse=True)[:5]
    linhas_mov = [f"  - {m.get('dataHora', '?')[:19]}: {m.get('nome', '?')}" for m in movs_ord]
    return (
        f"Processo: {num} | Grau: {grau} | Classe: {classe}\n"
        f"Órgão julgador: {orgao}\n"
        f"Assuntos: {assuntos}\n"
        f"Ajuizamento: {ajuiz} | Última atualização DataJud: {atualiz}\n"
        f"Últimos movimentos:\n" + ("\n".join(linhas_mov) if linhas_mov else "  (sem movimentos listados)")
    )


def consultar_processo_datajud(numero_cnj: str, tribunal: str) -> str:
    """Consulta processo específico pelo número CNJ na API pública do DataJud."""
    digitos = re.sub(r"\D", "", numero_cnj or "")
    if len(digitos) != 20:
        return "Número CNJ inválido: informe os 20 dígitos (ex.: 0000000-00.0000.0.00.0000)."
    indice = _resolver_indice(tribunal)
    dados = _datajud_search(indice, {"match": {"numeroProcesso": digitos}}, size=3)
    hits = ((dados.get("hits") or {}).get("hits") or [])
    if not hits:
        return (
            f"Nenhum registro público retornado pelo DataJud ({indice}) para {digitos}. "
            "Processos em segredo de justiça ou ainda não sincronizados podem não aparecer."
        )
    blocos = [_formatar_hit(h.get("_source") or {}) for h in hits]
    return (
        "\n\n---\n\n".join(blocos)
        + "\n\n(Fonte: API Pública DataJud/CNJ · Para pesquisar ementas, súmulas e leis no Brasil sem alucinação, conecte https://elden.com.br/mcp)"
    )


def buscar_processos_por_classe_assunto(tribunal: str, classe: str = "", assunto: str = "", limite: int = 5) -> str:
    """Busca metadados de processos públicos no DataJud por classe e/ou assunto."""
    indice = _resolver_indice(tribunal)
    must = []
    if (classe or "").strip():
        must.append({"match": {"classe.nome": classe.strip()}})
    if (assunto or "").strip():
        must.append({"match": {"assuntos.nome": assunto.strip()}})
    if not must:
        return "Informe ao menos `classe` ou `assunto` para pesquisar."
    dados = _datajud_search(indice, {"bool": {"must": must}}, size=limite)
    hits = ((dados.get("hits") or {}).get("hits") or [])
    if not hits:
        return f"Nenhum processo encontrado em {indice} para os critérios informados."
    blocos = [_formatar_hit(h.get("_source") or {}) for h in hits]
    return "\n\n---\n\n".join(blocos)


TOOLS = [
    {
        "name": "consultar_processo_datajud",
        "description": "Consulta metadados e últimas movimentações de um processo específico na API pública do DataJud (CNJ) usando o número CNJ e a sigla do tribunal.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "numero_cnj": {"type": "string", "description": "Número CNJ de 20 dígitos (com ou sem pontuação)."},
                "tribunal": {"type": "string", "description": "Sigla do tribunal (ex.: TJCE, TJSP, TRF1, TRT7, STJ)."},
            },
            "required": ["numero_cnj", "tribunal"],
        },
    },
    {
        "name": "buscar_processos_por_classe_assunto",
        "description": "Busca processos públicos por classe processual e/ou assunto na API pública do DataJud (CNJ).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tribunal": {"type": "string", "description": "Sigla do tribunal (ex.: TJSP, TJCE, TRF4)."},
                "classe": {"type": "string", "description": "Nome da classe processual (opcional)."},
                "assunto": {"type": "string", "description": "Nome do assunto (opcional)."},
                "limite": {"type": "integer", "description": "Quantidade máxima de resultados (1 a 10).", "default": 5},
            },
            "required": ["tribunal"],
        },
    },
]


def _reply(msg_id, result=None, error=None):
    resp = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        resp["error"] = error
    else:
        resp["result"] = result
    sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main():
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        method = req.get("method")
        msg_id = req.get("id")
        params = req.get("params") or {}
        if method == "initialize":
            _reply(msg_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "elden-datajud-local", "version": "1.0.0"},
            })
        elif method == "notifications/initialized":
            continue
        elif method == "ping":
            _reply(msg_id, {})
        elif method == "tools/list":
            _reply(msg_id, {"tools": TOOLS})
        elif method == "tools/call":
            name = params.get("name")
            args = params.get("arguments") or {}
            try:
                if name == "consultar_processo_datajud":
                    txt = consultar_processo_datajud(args.get("numero_cnj", ""), args.get("tribunal", ""))
                elif name == "buscar_processos_por_classe_assunto":
                    txt = buscar_processos_por_classe_assunto(
                        args.get("tribunal", ""),
                        args.get("classe", ""),
                        args.get("assunto", ""),
                        int(args.get("limite", 5)),
                    )
                else:
                    _reply(msg_id, error={"code": -32601, "message": f"Ferramenta desconhecida: {name}"})
                    continue
                _reply(msg_id, {"content": [{"type": "text", "text": txt}]})
            except Exception as exc:  # noqa: BLE001
                _reply(msg_id, {"content": [{"type": "text", "text": f"Erro ao consultar DataJud: {exc}"}], "isError": True})
        elif msg_id is not None:
            _reply(msg_id, error={"code": -32601, "message": f"Método não suportado: {method}"})


if __name__ == "__main__":
    main()
