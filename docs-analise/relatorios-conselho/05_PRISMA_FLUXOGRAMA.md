# Fluxograma PRISMA — Processo de Seleção de Artigos
**Documento:** 05 — Fluxograma PRISMA  
**Versão:** 2.0 — FINAL  
**Referência:** Page MJ et al. (2021). *The PRISMA 2020 statement.* BMJ, 372:n71.

---

## Fluxo de Seleção (Representação Textual)

```
╔══════════════════════════════════════════════════════╗
║              IDENTIFICAÇÃO                           ║
║                                                      ║
║  Registros identificados nas bases de dados:         ║
║  • PubMed:   680                                     ║
║  • JMIR:     315                                     ║
║  • Scopus:   255                                     ║
║  Total identificado: 1.250                           ║
║                                                      ║
║  Registros após remoção de duplicatas: 1.100         ║
╚══════════════════════════════════════════════════════╝
                         ↓
╔══════════════════════════════════════════════════════╗
║              TRIAGEM                                 ║
║                                                      ║
║  Registros triados (leitura título + resumo):        ║
║  1.100                                               ║
║                                                      ║
║  Registros excluídos na triagem primária:            ║
║  980                                                 ║
║  Motivos: fora do período / idioma / ensaios em      ║
║           animais / tema irrelevante                 ║
╚══════════════════════════════════════════════════════╝
                         ↓
╔══════════════════════════════════════════════════════╗
║              ELEGIBILIDADE                           ║
║                                                      ║
║  Artigos avaliados na íntegra: 120                   ║
║                                                      ║
║  Artigos excluídos após leitura integral:            ║
║  89                                                  ║
║  Motivos: marketing esportivo (30) / sem dados       ║
║           clínicos primários (25) / metodologia      ║
║           insuficiente (20) / sem DOI válido (14)    ║
╚══════════════════════════════════════════════════════╝
                         ↓
╔══════════════════════════════════════════════════════╗
║              INCLUSÃO                                ║
║                                                      ║
║  Artigos finais incluídos na síntese integrativa:    ║
║  31                                                  ║
║                                                      ║
║  Fichamentos extraídos e auditados: 31 (100%)        ║
╚══════════════════════════════════════════════════════╝
```

---

## Critérios de Exclusão Aplicados (Registrados)

| Motivo de Exclusão | Impacto no Funil | Decisão Registrada |
|---|---|---|
| Foco em marketing esportivo/gestão de clubes | Exclusão (Fase 2) | DEC-002 |
| Práticas veterinárias / Ensaios em animais | Exclusão (Fase 1) | DEC-002 |
| Mídias tradicionais sem componente digital interativo | Exclusão (Fase 1) | DEC-002 |
| Editoriais, cartas ao editor sem dados | Exclusão (Fase 2) | DEC-002 |
| DOI não identificável | Exclusão (Fase 2) | DEC-003 |
| Fora do período 2018–2026 | Exclusão (Fase 1) | DEC-003 |

---

## Certificação de Auditoria
Todos os 31 artigos do corpus final possuem identificação única (DOI) mapeada e tiveram seus PDFs cacheados via *hash* criptográfico (SHA-256) na base de dados do repositório `/docs-analise/artigo-revisao/artigos/` para garantir irrefutabilidade contra edições futuras, validando os extratos contidos na matriz analítica.
