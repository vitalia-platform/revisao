# Metodologia e Progresso: Revisão Integrativa Vitalia (2018-2026)

Este documento descreve o rigor metodológico e o estado atual do trabalho de pesquisa bibliográfica para a plataforma Vitalia.

## 1. Escopo da Revisão
**Título:** O Impacto das Tecnologias Digitais de 3ª Geração no Exercício Físico e Saúde: Uma Revisão Integrativa (2018-2026).

**Objetivo:** Sintetizar as evidências mais recentes sobre Inteligência Artificial, Wearables de alta precisão e Realidade Virtual para fundamentar os algoritmos fisiológicos (Motor Kim/Keytel) da Vitalia.

### Estratégia PCC (População, Conceito, Contexto)
- **População:** Indivíduos praticantes de exercício físico, desde atletas até populações clínicas (pós-AVC, idosos).
- **Conceito:** Tecnologias digitais emergentes (IA Generativa, Machine Learning, Sensores PPG/ECG, Gamificação).
- **Contexto:** Cenário global pós-2018, com foco na convergência entre saúde digital e performance física.

---

## 2. Metodologia de Coleta e Organização

### Busca e Filtragem
- **Base de Dados Principal:** PubMed / PMC (NCBI).
- **Filtros Aplicados:** 
  - Período: 2018 – 2026.
  - Idioma: Inglês e Português.
  - Acesso: Free Full Text (Open Access).
- **Identificação:** Uso de **PMIDs (PubMed IDs)** como âncoras permanentes para evitar a volatilidade de links diretos de PDFs.

### Estrutura de Repositório (`docs-analise/artigo-revisao/`)
O material foi organizado de forma modular para processamento por agentes de IA:
- `artigos/`: Repositório central de PDFs (30+ arquivos validados).
- `fichamentos/`: Destino das análises técnicas individuais.
- `scripts/`: Ferramentas de automação para download e verificação.
- `lista_links_manual.md`: Guia de curadoria com 30 artigos de alto impacto verificados manualmente.
- `bibliografia_proposta_50.md`: Mapa temático com 55 referências divididas em 6 eixos.

---

## 3. Trabalho Realizado até Agora

1.  **Mapeamento Temático:** Divisão da literatura em eixos críticos:
    - **Eixo 1:** IA e Machine Learning (Chatbots, Prescrição via LLMs).
    - **Eixo 2:** Wearables e Sensores (Validação de Polar H10, Apple Watch, Garmin).
    - **Eixo 3:** Mobile Apps e mHealth (Gamificação e Adesão).
    - **Eixo 4:** Exergames e VR (Reabilitação e Intensidade Percebida).
    - **Eixo 5:** Telemetria e HITL (Human-in-the-Loop).
2.  **Consolidação de Dados:** 
    - Identificação de duplicidade e limpeza de estrutura de pastas aninhadas.
    - Remoção de arquivos corrompidos/vazios (bloqueios de servidor).
    - Unificação de PDFs em diretório canônico.
3.  **Validação de Acesso:** Verificação manual de links para garantir que o processo de "fichamento" não seja interrompido por erros de 404.

---

## 4. Próximos Passos (Workflow Científico)

1.  **Fichamento Técnico (P0):** Acionamento do agente `research-analyst` para processar os PDFs da pasta `artigos/` e gerar sumários estruturados em `fichamentos/`.
2.  **Síntese de Evidências:** Agrupar os achados por eixo temático para extrair constantes fisiológicas.
3.  **Extração de Constraints:** Transformar a ciência em regras de código para o backend da Vitalia (HITL Médico).

> [!IMPORTANT]
> Todos os arquivos estão agora organizados em `docs-analise/artigo-revisao/`. A limpeza de arquivos 0B foi concluída com sucesso.
