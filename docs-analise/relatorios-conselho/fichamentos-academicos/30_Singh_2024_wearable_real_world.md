# FICHAMENTO #30 — [REVISÃO CIENTÍFICA PENDENTE]

> Esta informação é educacional. Conteúdo destinado a pesquisadores. Revisão científica obrigatória antes de uso clínico.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA

| Campo | Dados |
|---|---|
| **Autores** | Singh B, Chastin S, Miatke A, Curtis R, Dumuid D, Brinsley J, Ferguson T, Szeto K, Simpson C, Eglitis E, Willems I, Maher C |
| **Título** | Real-World Accuracy of Wearable Activity Trackers for Detecting Medical Conditions: Systematic Review and Meta-Analysis |
| **Periódico** | JMIR mHealth and uHealth |
| **Ano** | 2024 |
| **Volume/Páginas** | 12:e56972 |
| **DOI** | 10.2196/56972 |
| **Tipo de estudo** | Revisão sistemática e meta-análise |
| **Registro PROSPERO** | CRD42023407867 |
| **Categoria analítica** | **H — Machine Learning e HAR em Wearables (Diagnóstico)** |

---

## 2. QUESTÃO DE PESQUISA / OBJETIVO

Avaliar a confiabilidade e a acurácia de rastreadores de atividade comercialmente disponíveis (como Fitbit, Apple Watch, Oura Ring) para a detecção de doenças e eventos médicos operando exclusivamente em **condições de vida real (free-living)**, sem o controle rígido de laboratórios clínicos.

---

## 3. METODOLOGIA

Revisão sistemática com meta-análise avaliando métricas diagnósticas (sensibilidade, especificidade, área sob a curva - AUC, valor preditivo positivo - VPP).
- **Inclusão:** População adulta (>18 anos) em ambiente "free living". Uso de um rastreador de atividade wearable. Detecção de condições médicas com validação clínica.
- **Corpus:** 28 estudos (1.226.801 participantes). Destes:
  - 16 avaliaram COVID-19.
  - 5 avaliaram Fibrilação Atrial (AF).
  - 3 avaliaram quedas (falls).
- **Dispositivos mais frequentes:** Apple Watch, Fitbit, Oura Ring.

---

## 4. RESULTADOS PRINCIPAIS

### Detecção de Fibrilação Atrial (O Padrão Ouro)
- **Desempenho:** Sensibilidade altíssima de **94.2%** e Especificidade de **95.3%**.
- Valor Preditivo Positivo (VPP): 87.4% (indicando que a maioria dos alertas positivos reflete uma condição clínica real).
- A acurácia algorítmica para AF já se equipara à sensibilidade do ECG tradicional de 12 derivações (que varia entre 93-97%).

### Detecção de Quedas (Fall Detection)
- **Desempenho:** Sensibilidade moderada-alta (**81.9%**), mas com Especificidade problemática de **62.5%**.
- **Problema:** A taxa de "falsos positivos" em quedas (especificidade baixa) é gerada por movimentos rápidos dos braços que mimetizam a desaceleração de uma queda para os acelerômetros de pulso, resultando em alarmes desnecessários em ambiente real.

### Detecção de Infecção Viral (COVID-19)
- **Desempenho:** AUC consolidada de 80.2%. Sensibilidade (79.5%) e Especificidade (76.8%).
- A detecção viral não tem "padrão-ouro" via sensores mecânicos, mas opera inferindo dados preditivos de FC de repouso, HRV e temperatura epidérmica.

---

## 5. ACHADOS CRÍTICOS

> **[REVISÃO CIENTÍFICA PENDENTE]** — Embora a detecção de Fibrilação Atrial seja matematicamente robusta, clínicos expressam forte preocupação com o aumento brutal de "falsos positivos" gerados em escala populacional, sobrecarregando hospitais com pacientes assintomáticos ansiosos.

1. **Hiper-Especialização vs Uso Geral:** Dispositivos comerciais atuais já operam como equipamentos médicos (FDA approved) para o coração (sensores ópticos PPG precisos), porém ainda falham em testes mecânicos puros como detecção de quedas fora do laboratório, devido ao excesso de ruído do uso rotineiro do pulso.
2. **Diagnóstico "Em Branco":** Foi uma descoberta notável para os autores que, embora o mercado venda wearables que medem desde "estresse" até "apneia do sono", praticamente **não existem estudos de acurácia free-living** fora da trindade de COVID, coração e quedas. Grande parte do marketing de saúde de wearables é suportada apenas por dados isolados de laboratório (in vitro).

---

## 6. RELEVÂNCIA PARA A REVISÃO

Este artigo encerra brilhantemente a análise da Categoria H (Sensores Passivos). Ele evidencia que, para a meta de reabilitação/geriatria, o uso passivo do relógio tem um gap: a predição de quedas falha em ambientes reais (62.5% de especificidade) porque sensores de pulso sofrem muita interferência de ruído diário. A arquitetura de hardware precisa evoluir ou ser migrada para sensores na cintura se a prioridade for a monitorização biomecânica do idoso (e não apenas o ritmo cardíaco). Isso valida as constatações de Wang (#10) e Piau (#12).

---

## 7. EXTRATO PARA SÍNTESE

> *"While wearable activity trackers show remarkable accuracy in identifying atrial fibrillation (sensitivity 94.2%, specificity 95.3%) in free-living settings, their performance in fall detection shows lower specificity (62.5%), highlighting a significant problem with false positives outside controlled laboratory conditions."* — Singh et al., 2024

**Resultado-chave:** Meta-análise gigantesca (N=1.22 milhões) prova que relógios comerciais atingem o nível do ECG para fibrilação atrial (95% de especificidade), mas falham drasticamente na predição de quedas biomecânicas na vida real devido a altas taxas de falsos positivos induzidos pelo uso no pulso.

---

## 8. METADADOS

| Campo | Valor |
|---|---|
| **Data** | 2026-05-13 |
| **Status** | DRAFT — [REVISÃO CIENTÍFICA PENDENTE] |
| **Lote** | 4 — Finalização do Corpus |
| **Arquivo PDF** | `2024 - JMIR - 10.2196_39231.pdf` |
