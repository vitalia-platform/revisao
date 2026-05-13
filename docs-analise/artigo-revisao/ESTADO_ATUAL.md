# Estado Atual da Revisão Integrativa — 12/05/2026

## 📊 Status do Lote 1 (Concluído)
O primeiro lote de artigos (Eixos 1 e 6) focado em **Wearables, Sensores e Dados Fisiológicos** foi totalmente processado.

### Artigos Fichados (7/31):
1.  **Ferguson 2022** (10.1016/S2589-7500(22)00111-X) — Validação de wearables comerciais.
2.  **Germini 2022** (10.2196/35060) — Acurácia de apps de VFC.
3.  **Kristoffersson 2022** (10.3390/s22031101) — VFC em idosos e doentes crônicos.
4.  **Blount 2021** (10.3390/jcm10112446) — Feedback em tempo real para sobreviventes de câncer.
5.  **Zhang 2022** (10.3390/s22041476) — Deep Learning (CNN/LSTM) para HAR.
6.  **Manresa-Rocamora 2021** (10.3390/ijerph181910299) — Metanálise de treino guiado por VFC.
7.  **Fuller 2020** (10.2196/18694) — Validação de passos/FC/Kcal em wearables comerciais.

## ⚙️ Implicações para os Motores Vitalia
### Motor Kim (Fisiológico)
- **Métrica Primária:** RMSSD (VFC) com média móvel de 7 dias para baseline.
- **Arquitetura:** Modelos híbridos CNN-LSTM para reconhecimento de atividade física via BLE (Kotlin).
- **Segurança:** Implementação de Federated Learning para preservar privacidade dos dados cardíacos.

### Motor Keytel (Comportamental)
- **Restrição:** Ignorar métricas de calorias de terceiros; usar apenas FC/Tempo para cálculo de carga.
- **Nudges:** Acionamento de feedback tátil e orientações de recuperação baseadas no Coeficiente de Variação (CV) da VFC.

## 🚀 Próximos Passos (Lote 2)
- **Objetivo:** Processar o Lote 2 (Gamificação e Apps Móveis).
- **Foco:** Extrair mecânicas de retenção e engajamento.

## 🛡️ Auditoria e Integridade
- Todos os arquivos PDFs foram renomeados e auditados no `AUDIT_LOG.json` via SHA-256.
- O draft inicial do artigo acadêmico está em `artigo_vitalia_draft.md`.
