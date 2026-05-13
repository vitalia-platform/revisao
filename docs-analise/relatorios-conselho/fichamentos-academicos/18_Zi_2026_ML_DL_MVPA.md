# FICHAMENTO #18 — [REVISÃO CIENTÍFICA PENDENTE]

> Esta informação é educacional. Conteúdo destinado a pesquisadores. Revisão científica obrigatória antes de uso clínico.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA

| Campo | Dados |
|---|---|
| **Autores** | Zi Y, van de Ven SRB, de Geus EJC, Chen P |
| **Título** | Machine and Deep Learning for Detection of Moderate-to-Vigorous Physical Activity From Accelerometer Data: Systematic Scoping Review |
| **Periódico** | Interactive Journal of Medical Research (IJMR) |
| **Ano** | 2026 |
| **Volume/Páginas** | 15:e76601 |
| **DOI** | 10.2196/76601 |
| **Tipo de estudo** | Scoping review sistemática (PRISMA-ScR; Arksey & O'Malley framework) |
| **Categoria analítica** | **H — Machine Learning e Acelerometria** |

---

## 2. QUESTÃO DE PESQUISA / OBJETIVO

Sintetizar evidências sobre técnicas de ML e DL para detecção de AFMV (atividade física moderada a vigorosa) a partir de dados de acelerômetro, com foco em: (1) performance dos modelos; (2) viés algorítmico; (3) configurações de sensores; (4) potencial translacional.

**6 questões de pesquisa:**
1. Quais técnicas ML/DL são usadas para detecção de AFMV?
2. Como a configuração do sensor (posição, sampling rate) influencia o desempenho?
3. Qual a magnitude do gap laboratório vs. vida-livre?
4. Como os protocolos de validação variam e limitam a comparabilidade?
5. Em que extensão há viés algorítmico contra idosos/populações clínicas?
6. Que proporção de estudos adere a práticas de ciência aberta?

---

## 3. METODOLOGIA

### Bases de dados
PubMed, IEEE Xplore, Web of Science (fevereiro/1995–abril/2025) + citation tracking manual.

### Critérios de inclusão
- Estudos que aplicaram ML ou DL
- Uso de acelerometria (qualquer posição/dispositivo)
- AFMV como desfecho
- Humanos (qualquer idade/condição)
- Artigos peer-reviewed em inglês

### Critérios de exclusão
- Sem ML/DL; sensores multimodais com FC; contextos não-AF; somente sedentarismo vs. não-sedentarismo; modelos teóricos sem validação empírica

---

## 4. RESULTADOS PRINCIPAIS

### Seleção
- 1.938 artigos triados → **40 estudos incluídos** (36 + 4 busca manual)

### Performance dos modelos

#### ML Tradicional (random forest, SVM)
| Métrica | Lab | Vida-livre |
|---|---|---|
| F1-score | 87,4%–100% | ↓ 8,0%–13,3% |
| Acurácia | 87,9%–100% | ↓ 6,6%–12,2% |

#### Deep Learning (CNN, Transformers)
| Métrica | Vida-livre |
|---|---|
| F1-score | 71,9%–79,8% |
| Acurácia | 87,9%–100% |

#### Modelos Híbridos (CNN-LSTM) — estado da arte
| Métrica | Resultado |
|---|---|
| F1-score | **91,4%–98,4%** |
| Acurácia | **97,7%–99,0%** |

### Configuração de sensores
- **Wrist-worn**: dominante (30/40 estudos; 75%)
- Wrist ≈ hip em lab (F1: 86,5%–88,6%)
- **Multissensores (wrist + hip)**: maior acurácia (89,7%)

### Viés algorítmico
- Modelos treinados em adultos jovens saudáveis **subestimam AFMV em idosos**
- Apenas 17/40 (42,5%) compartilham código e dados — "novo dilema dos cut-points"

### Ciência aberta
- Apenas 42,5% dos estudos com código/dados disponíveis
- Fragmentação dos protocolos de validação impossibilita comparação entre estudos

---

## 5. ACHADOS CRÍTICOS

> **[REVISÃO CIENTÍFICA PENDENTE]** — Métricas de desempenho são contextuais (população, sensor, ambiente); não aplicar thresholds sem validação específica.

1. **Gap lab → vida-livre**: principal desafio translacional; modelos que funcionam em laboratório degradam ~10% no mundo real
2. **CNN-LSTM como arquitetura ideal**: combina extração de padrões espaciais (CNN) com modelagem temporal (LSTM) — superior para dados contínuos de acelerômetro
3. **Wrist-worn como posição dominante**: conveniência do uso real, mas acurácia ligeiramente inferior ao hip em lab; multissensor como solução
4. **Viés de equidade**: algoritmos não generalizáveis para idosos/populações clínicas comprometem aplicabilidade em saúde pública
5. **Oportunidades emergentes**: edge computing (processamento no dispositivo) e modelos híbridos com dados contextuais

---

## 6. RELEVÂNCIA PARA A REVISÃO

### Contribuição para o corpus
- Fundamenta a **Categoria H** (ML e Acelerometria) do mapeamento
- Conecta-se diretamente ao debate sobre **validade dos wearables** (Artigo 21) e **HAR por smartphone** (Artigo 22)
- Diferencia claramente ML tradicional vs. DL vs. modelos híbridos — útil para a síntese sobre estado da arte tecnológico

### Tensões com outros artigos do corpus
- Complementa Fuller et al. (2020, #21): enquanto #21 testa validade de dispositivos comerciais por comparação direta, #18 mostra que ML/DL superam cut-points tradicionais para classificação de AFMV

### Posicionamento PICO
| | |
|---|---|
| **P** | Humanos (qualquer faixa etária/condição) |
| **I** | Algoritmos ML/DL sobre dados de acelerômetro |
| **C** | Métodos tradicionais de cut-points; calorimetria indireta |
| **O** | Acurácia de classificação de AFMV (F1-score, accuracy) |

---

## 7. EXTRATO PARA SÍNTESE

> *"ML and DL significantly enhance MVPA monitoring by automating feature extraction and improving adaptability to free-living variability. However, persistent gaps in generalizability, inconsistent validation protocols, and transparency deficits hinder translation."* — Zi et al., 2026, p.1

**Resultado-chave:** Modelos híbridos CNN-LSTM atingem F1=91–98% — estado da arte; mas apenas 42,5% dos estudos são reprodutíveis.

---

## 8. METADADOS DE CONTROLE

| Campo | Valor |
|---|---|
| **Fichamento elaborado por** | Agente acadêmico (IA) |
| **Data** | 2026-05-13 |
| **Status** | DRAFT — [REVISÃO CIENTÍFICA PENDENTE] |
| **Lote** | 3 — IA, Telehealth e Wearables |
| **Arquivo PDF** | `2026 - IJMR - 10.2196_76601.pdf` |
