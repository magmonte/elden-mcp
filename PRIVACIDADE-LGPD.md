# Segurança, Criptografia, Privacidade e LGPD (OAB / CNJ)

> **Resumo para advogados:** O Elden foi construído para que advogados e escritórios possam pesquisar jurisprudência com tranquilidade e respaldo técnico: conta com **criptografia em trânsito e em repouso**, **isolamento por usuário**, **recomendação de não envio de dados sensíveis** e **compromisso expresso de nunca comercializar nenhum dado**.

---

## 1. Criptografia e Segurança Técnica

- **Criptografia em trânsito (HTTPS / TLS):** toda comunicação com o site e com o servidor MCP (`https://elden.com.br/mcp`) é trafegada exclusivamente por conexões cifradas com proteção de borda.
- **Criptografia em repouso (memória contextual):** anotações de memória contextual gravadas pelo usuário são armazenadas **de forma cifrada e isoladas por conta**.
- **Credenciais e tokens protegidos por hash:** chaves de API e tokens de acesso OAuth/sessão são armazenados de forma irreversível (*hash*), nunca em texto puro, com **revogação em tempo real** pelo painel do usuário.
- **Backups cifrados e logs limpos:** cópias de segurança são armazenadas de forma cifrada, e os registros operacionais de telemetria omitem credenciais e o conteúdo de consultas.
- **Sem cookies de rastreamento ou anúncios:** utilizamos apenas cookies estritamente necessários para autenticação e sessão.

Consulte também a nossa [Política de Segurança (SECURITY.md)](./SECURITY.md).

---

## 2. Minimização Estrita: Recomendamos Não Enviar Dados Sensíveis

- Quando você conversa no Claude, ChatGPT ou outro assistente, o texto integral dos autos e documentos anexados permanece exclusivamente no ambiente do provedor de IA que você escolheu.
- Ao consultar o Elden via MCP, a IA envia ao endpoint `https://elden.com.br/mcp` **apenas os parâmetros objetivos da consulta** (termos de busca jurisprudencial, número de referência, dispositivo legal ou anotações explicitamente salvas por você).
- **Recomendação de boas práticas:** como é o próprio assistente de IA quem formula os termos da busca durante a conversa, **recomendamos não enviar dados pessoais sensíveis, nomes de partes, CPF/RG, segredos de justiça ou autos integrais** — formule a pesquisa em **tese jurídica**, mantendo o sigilo profissional ponta a ponta.

---

## 3. Compromisso Expresso: Zero Comercialização de Dados

Mesmo que algum dado sensível ou identificador acabe sendo incluído por engano em uma consulta ou anotação:

- **Não comercializamos nenhum dado:** o Elden **não vende, não aluga, não cede para corretores de dados ou redes de publicidade e não comercializa** dados cadastrais, termos de consulta, estilos de redação ou memórias de usuários.
- **Não há compartilhamento cruzado entre contas:** suas anotações de memória e preferências de estilo são isoladas por usuário e nunca ficam visíveis para outros advogados ou escritórios.
- **Controle e exclusão pelo titular:** você pode consultar, apagar suas memórias e estilos ou revogar conexões OAuth imediatamente no painel da conta, além de poder solicitar remoção/exclusão pelos canais de suporte.

---

## 4. Uso Seguro na Advocacia (OAB, CNJ e LGPD)

- **Sigilo profissional (art. 7º, II, da Lei nº 8.906/1994):** a arquitetura sem upload de autos integrais, somada à criptografia e ao isolamento por conta, preserva o sigilo dos documentos do cliente no ambiente de escolha do advogado.
- **Recomendação CFOAB nº 001/2024 e Resolução CNJ nº 615/2025:** o Elden atua como ferramenta de apoio à verificação de fontes oficiais (entregando link direto do tribunal, número do processo e enunciado) para sustentar a **supervisão humana obrigatória**. Quem redige, confere o inteiro teor antes de protocolar e assume a responsabilidade técnica pela peça é sempre o advogado.

---

## 5. Controlador, Revisão e Suporte Humano

- **Controlador / Encarregado (LGPD):** Pacheco Monteiro Advocacia (Fortaleza/CE) — Saulo Magalhães Monteiro ([contato@elden.com.br](mailto:contato@elden.com.br)).
- **Documento vigente:** Política de Privacidade v1.0 (12/11/2026) disponível integralmente em [elden.com.br/privacidade](https://elden.com.br/privacidade).
