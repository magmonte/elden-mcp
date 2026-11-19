# Changelog — Elden (`elden.com.br`)

Registro público de evolução do serviço MCP, acervo jurídico, modelos próprios e documentação de integração do **Elden** (`https://elden.com.br/mcp`).

---

## [v2.0.0] — 2026-11-19
### IAs Próprias Completas em Produção (Embedding + Rerank), Benchmarks e Patch de Precisão
- **Arquitetura proprietária completa em produção:** Entra no ar o **modelo próprio de *embedding* jurídico do Elden**, operando em conjunto com o **modelo próprio de *rerank* jurídico** em dois estágios sobre mais de 11 milhões de acórdãos puros da base vetorial principal (dentro do acervo de 20M+ publicações oficiais), legislação federal, súmulas/temas vinculantes e doutrina.
- **Desempenho comprovado contra referências abertas (benchmark caixa-preta em subcorpus congelado + 12.310 artigos de lei):**
  - Pipeline completo (**Elden-Model + Reranker**) alcança **`58,76%` de MRR@10 médio** nos três eixos (**`53,41%`** em consultas reais `T1` com `R@10 = 86,08%`, **`47,27%`** multi-área `T2` e **`75,59%`** em legislação com `R@10 = 85,07%`), superando `Qwen3-Embedding-4B` (`52,05%`), `Qwen3-Embedding-8B` (`50,47%`), `BAAI/bge-m3` (`46,16%`) e `intfloat/multilingual-e5-large` (`44,36%`).
  - Em **escala real (11+ milhões de acórdãos)**: **3× mais acerto no topo (`R@1`: `0,37% → 1,10%`)** e **+109% em `R@10`** (`4,03% → 8,42%`) frente à geração anterior com reordenação, recuperação inicial em **`43,5 ms` (p50)**, resposta completa em dois estágios em **`~1,47 s` (p50)** e **`100%` dos precedentes verificáveis** diretamente na base oficial.
- **Patch v2.0 de precisão e UX jurídica (testes ao vivo):**
  - **Ordenação de leis (`buscar_lei`):** corrigido bug crítico na chave de ordenação pós-rerank, devolvendo dispositivos processuais e materiais exatos ao topo (ex.: CPC art. 248 em citação postal com AR), além da correção ortográfica no rodapé de pertinência.
  - **Súmulas e Temas:** busca vetorial aprimorada com reforço por itens numerados de súmulas/temas longos e calibragem do reordenador para destacar teses vinculantes aplicáveis (ex.: Tema 566 do STJ em prescrição intercorrente).
  - **Agrupamento e limpeza de enunciados:** temas com enunciado rigorosamente idêntico passam a ser agrupados em um único bloco (ex.: *Temas 1154 / 1241 do STJ*), com correção pontual de travessão (`—`).
  - **Prioridade para enunciados vigentes:** súmulas e teses canceladas/superadas deixam de ocupar vagas em buscas temáticas livres (salvo quando pedidas explicitamente), mantendo o alerta `⚠️ CANCELADA` na conferência direta por número (`verificar_citacao`).
  - **Panorama de fundamentação (`buscar_fundamentacao`):** eliminada a duplicação de acórdãos entre os blocos de súmulas/temas e julgados nacionais, eliminada a contenção interna entre os eixos (preservando busca semântica completa em leis, súmulas e acórdãos) e ajustado o corte por caracteres para nunca exibir cabeçalho sem ementa.

---

## [v1.2.0] — 2026-11-17
### Super-Ferramenta de Fundamentação & Nova Matriz de Planos
- **Nova super-ferramenta `buscar_fundamentacao`:** Executa varredura combinada em três eixos (legislação federal, súmulas/temas vinculantes verificados e acórdãos da base nacional) e entrega um dossiê compactado com pontos principais e identificadores exatos para aprofundamento item a item (`buscar_lei`, `verificar_citacao`, `verificar_processo`). Disponível em modo degustação no **Grátis** (até **2 usos a cada 5 horas**) e liberada com maior profundidade no **Essencial** e **Profissional**.
- **Estilos de escrita personalizados exclusivos para assinantes:** O plano **Grátis** utiliza o estilo forense padrão em modo somente leitura; criar e editar estilos próprios (`estilo_criar`, `estilo_editar`) agora faz parte dos planos **Essencial** (até 5 estilos, inclusive a partir de PDF seu) e **Profissional** (até 20 estilos, inclusive a partir de PDF seu).
- **Ferramentas estratégicas e profundidade por busca:** `dossie_precedente`, `pesquisar_questao` e `conferir_transcricao` passam a integrar os planos **Essencial** e **Profissional**. A profundidade máxima por consulta foi calibrada em **3** resultados/busca no **Grátis**, **8** no **Essencial** e **15** no **Profissional**.
- **Memória entre conversas no Essencial:** O plano **Essencial** passa a incluir memória persistente para até **100 anotações** (e o **Profissional** amplia para até **5.000 anotações**).
- **Adiantamento de limite e aviso direto pela IA:** O adiantamento da janela de 5 horas fica exclusivo dos planos pagos (**Essencial** e **Profissional**). Ao atingir o teto no plano **Grátis**, a própria IA avisa o advogado o horário de renovação e as opções de upgrade.

---

## [v1.1.0] — 2026-11-16
### Produto, Acervo e IAs Próprias
- **Acervo:** Expansão contínua das publicações dos tribunais brasileiros (STF, STJ, TJs, TRFs via DJEN) e legislação do Planalto.
- **1ª Geração de IAs Próprias:** Operação com modelo próprio de *rerank* jurídico para ordenação por relevância jurídica e desenvolvimento ativo do modelo próprio de *embedding* jurídico para o vocabulário do Direito brasileiro.
- **Limites e Planos:** Documentação pública detalhada do **Plano Grátis Permanente** (R$ 0, sem cartão, renovação em janelas de 5 horas e ciclos semanais), **adiantamento de limite** para picos de demanda e separação clara entre **histórico de pesquisas** (7 dias / 30 dias / 12 meses) e **memória entre conversas** (exclusiva dos planos Profissional e Escritório).

### Integrações e Ecossistema
- **ChatGPT:** Compatibilidade documentada para planos **Pro, Business, Enterprise e Edu** na versão web.
- **Claude:** Conexão OAuth de 1 clique compatível com todos os planos, inclusive o plano gratuito.
- **Documentação & GEO:** Publicação de [`llms.txt`](./llms.txt), [`server.json`](./server.json), [`mcp.json`](./mcp.json), [`README.en.md`](./README.en.md) e guias de privacidade/LGPD.
- **Diretórios MCP:** Submissão ao catálogo oficial de servidores MCP remotos (`punkpeye/awesome-remote-mcp-servers`).

---

## [v1.0.0] — 2026-11-16
- Lançamento inicial do repositório público de documentação e manifestos MCP do Elden (`https://github.com/magmonte/elden-mcp`).
- Guia de conexão OAuth para Claude, ChatGPT e clientes compatíveis (`CONECTAR.md`).
- Documentação de minimização de dados, LGPD e apoio à supervisão humana (Recomendação CFOAB nº 001/2024 e Resolução CNJ nº 615/2025).
