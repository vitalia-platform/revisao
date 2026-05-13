# FICHAMENTO #22 — [REVISÃO CIENTÍFICA PENDENTE]

> Esta informação é educacional. Conteúdo destinado a pesquisadores. Revisão científica obrigatória antes de uso clínico.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA

| Campo | Dados |
|---|---|
| **Autores** | Straczkiewicz M, James P, Onnela J-P |
| **Título** | A systematic review of smartphone-based human activity recognition methods for health research |
| **Periódico** | npj Digital Medicine |
| **Ano** | 2021 |
| **Volume/Páginas** | 4:148 |
| **DOI** | 10.1038/s41746-021-00514-4 |
| **Categoria analítica** | **H — Machine Learning e Reconhecimento de Atividade** |

---

## 2. OBJETIVO

Sistematizar abordagens de HAR (Human Activity Recognition) baseadas em smartphone, focando em aquisição, pré-processamento, extração de features e classificação de atividades, com ênfase em generalizabilidade e reprodutibilidade para pesquisa em saúde pública.

---

## 3. METODOLOGIA

Revisão sistemática metodológica; Scopus, PubMed, Web of Science (até dez/2020).  
**108 artigos incluídos** de 1.901 hits.

Critérios: artigos originais em inglês; uso de smartphone consumer-grade apenas; HAR sem equipamento auxiliar.

---

## 4. RESULTADOS PRINCIPAIS

### Sensores utilizados (N=108)
| Sensor | % |
|---|---|
| Acelerômetro | 97,2% |
| Giroscópio | 49,1% |
| GPS | 25,9% |

### Ambiente de medição
- Controlado (lab): 74,1%
- Free-living: **25,9%** (minoria)

### Localização do smartphone
- Lower body (bolso calça): 55,6% (posição dominante)

### Classificadores
- Métodos simples (SVM, k-NN, DT): 63%
- Ensemble (RF, AdaBoost): 35,2%
- Deep learning: 23,1%

### Reprodutibilidade — gap crítico
| Indicador | % |
|---|---|
| Código-fonte público | **3,7%** |
| Dataset público | 35,2% |
| Validação cross-coorte | 9,3% |

### Populações
- Maioria: adultos jovens saudáveis (20–30 anos); N típico <30 participantes
- Poucos estudos com idosos ou populações clínicas

---

## 5. ACHADOS CRÍTICOS

1. **Smartphone como instrumento HAR viável**: ubíquo (5 bilhões de usuários em 2020), sem hardware adicional
2. **Crise de reprodutibilidade**: apenas 3,7% com código público — pior que wearables research-grade
3. **74% laboratorial**: translação para free-living raramente validada
4. **Acelerômetro dominante**: sensor primário; giroscópio melhora atividades complexas
5. **Lacuna de diversidade**: jovens e saudáveis super-representados — generalização limitada

---

## 6. RELEVÂNCIA PARA A REVISÃO

Panorama metodológico de HAR por smartphone — base técnica para **Categoria H**.  
Complementa Zi et al. (#18, ML/DL para AFMV) com a perspectiva do smartphone como instrumento de coleta.  
Justifica uso de smartphones como alternativa democrática a wearables dedicados.

---

## 7. EXTRATO PARA SÍNTESE

> *"Smartphones are well-suited for HAR research in the health sciences. Future studies should focus on improving the quality of collected data, incorporate more diverse participants and share the source code."* — Straczkiewicz et al., 2021

**Resultado-chave:** 108 estudos; acelerômetro em 97%; código público em 3,7%; free-living em 26%.

---

## 8. METADADOS

| Campo | Valor |
|---|---|
| **Data** | 2026-05-13 |
| **Status** | DRAFT — [REVISÃO CIENTÍFICA PENDENTE] |
| **Lote** | 3 — IA, Telehealth e Wearables |
| **Arquivo PDF** | `2021 - BMC - 10.1186_s13102-021-00276-2.pdf` |
