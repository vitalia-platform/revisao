# Reasoning Log — Registro de Decisões do Agente
**Documento:** 02 — Reasoning Log  
**Propósito:** Transparência total do processo de análise conduzido pelo agente de IA. Cada entrada documenta uma decisão metodológica relevante com sua justificativa, evidência e impacto.  
**Audiência:** Conselho científico e de governança.

> [!IMPORTANT]
> Este documento é a prova de que o trabalho de IA foi conduzido de forma **metodologicamente controlada**, não como "caixa-preta". Cada decisão é rastreável.

---

## Convenção de Registro

```
[DEC-NNN] Tipo | Data | Decisão | Justificativa | Impacto
```

**Tipos:**
- `INCLUSÃO` — artigo aceito no corpus
- `EXCLUSÃO` — artigo rejeitado com motivo
- `CATEGORIZAÇÃO` — atribuição de categoria temática
- `METODOLÓGICA` — decisão sobre o método em si
- `REFORMULAÇÃO` — correção de curso em relação a trabalho anterior

---

## Decisões Registradas

---

### [DEC-001] METODOLÓGICA | 2026-05-13

**Decisão:** Reformulação completa do objetivo e do template de fichamento.

**Contexto:** A sessão anterior (2026-05-12) produziu fichamentos orientados ao desenvolvimento da plataforma Vitalia — com seções "Motor Kim", "Motor Keytel" e "Extração de Parâmetros de Produto". Esse modelo é inadequado para uma publicação acadêmica.

**Justificativa:** O artigo de referência (Oliveira et al., 2020, *Conexões*) demonstra que o objetivo correto é **mapear o campo de pesquisa**, não extrair parâmetros de produto. O método Mendes, Silveira e Galvão (2008) preconiza fichamentos descritivos e categorização indutiva, não prescritiva.

**Impacto:** 
- Os 7 fichamentos do Lote 1 serão integralmente refeitos.
- O artigo draft será reescrito com remoção da seção "Aplicação Prática: Fundamentos dos Motores Vitalia".
- O template de fichamento passa a ser puramente acadêmico.

---

### [DEC-002] METODOLÓGICA | 2026-05-13

**Decisão:** Adoção de categorias **emergentes** (abordagem indutiva), não pré-definidas.

**Contexto:** O trabalho anterior organizava os artigos em 6 eixos pré-definidos (Wearables, IA, Apps, Gamificação, Exergames, Telemetria). Isso é uma abordagem **dedutiva** — as categorias são impostas antes da leitura.

**Justificativa:** O método Mendes et al. (2008), combinado com o artigo modelo (Oliveira et al., 2020), preconiza que as categorias de uma revisão integrativa devem **emergir da leitura flutuante e em profundidade** dos textos. Oliveira et al. identificaram 4 categorias que não eram previsíveis a priori (mídias sociais, influenciadores digitais, tecnologias educacionais, exercícios mediados por tecnologia).

**Impacto:**
- Os 6 eixos pré-existentes são tratados como **hipóteses de trabalho**, não como categorias finais.
- A categorização final será feita após a leitura de todos os 31 artigos.
- O conselho científico validará as categorias emergentes antes da publicação.

---

### [DEC-003] METODOLÓGICA | 2026-05-13

**Decisão:** Período temporal definido como 2018–2026. Base primária: PubMed + JMIR + Scopus. Idioma primário: inglês.

**Justificativa:**
- O artigo modelo (Oliveira et al., 2020) cobriu 2013–2018. Esta revisão se posiciona como **atualização direta**, justificando o início em 2018.
- PubMed e JMIR concentram a maior produção sobre saúde digital, wearables e mHealth — as tecnologias predominantes no período.
- O foco em inglês é coerente com o periódico alvo internacional (JMIR, Frontiers in Digital Health).

**Impacto:** O fluxograma PRISMA registrará as buscas formais nessas três bases. Os 31 artigos do corpus atual precisam ter sua origem nas bases verificada.

---

### [DEC-004] METODOLÓGICA | 2026-05-13

**Decisão:** Estrutura de documentação adotada: Pacote Modular (Opção 1) + Registro de Decisões estilo ADR (Opção 3).

**Justificativa:** O trabalho será discutido em reunião de conselho com múltiplos perfis de membros (científico, clínico, técnico, governança). Documentos modulares permitem que cada membro leia apenas o que lhe compete. O reasoning log garante transparência do processo de IA.

**Impacto:** Criação de 6 documentos modulares em `docs-analise/relatorios-conselho/`.

---

### [DEC-005] CATEGORIZAÇÃO PROVISÓRIA | 2026-05-13

**Decisão:** Identificação de 4 categorias provisórias a partir da leitura do Lote 1 (7 artigos — wearables e sensores).

**Categorias provisórias identificadas:**
1. **Validação e Acurácia de Wearables** — Foco em testar a precisão de dispositivos comerciais (passos, FC, calorias) contra padrões-ouro laboratoriais.
2. **Monitoramento Fisiológico por VFC (HRV)** — Foco no uso da Variabilidade da Frequência Cardíaca como biomarcador para prescrição e recuperação.
3. **Reconhecimento de Atividade Física via Aprendizado de Máquina** — Foco em algoritmos CNN/LSTM aplicados a dados de acelerômetro para classificar movimentos.
4. **Tecnologia Digital em Populações Clínicas** — Foco em feedback digital (apps, wearables) para reabilitação de populações com condições específicas (câncer, doenças crônicas, idosos).

**Advertência metodológica:** Estas categorias são **provisórias e parciais**. O Lote 1 foi intencionalmente selecionado entre artigos de wearables e sensores — o corpus completo provavelmente revelará categorias adicionais (gamificação, apps, telereabilitação, IA generativa). A categorização final **não pode ser feita** com apenas 7 dos 31 artigos.

**Impacto:** Categorias registradas no `04_CATEGORIAS_ANALISE.md` com status "PROVISÓRIO".

---

### [DEC-006] INCLUSÃO | 2026-05-13

**Decisão:** Os 7 artigos do Lote 1 são **mantidos no corpus** após revisão do objetivo.

**Artigos:**
1. Ferguson et al. (2022) — DOI: 10.1016/S2589-7500(22)00111-X
2. Germini et al. (2022) — DOI: 10.2196/35060
3. Kristoffersson & Madhavan (2022) — DOI: 10.3390/s22031101
4. Blount et al. (2021) — DOI: 10.3390/jcm10112446
5. Zhang et al. (2022) — DOI: 10.3390/s22041476
6. Manresa-Rocamora et al. (2021) — DOI: 10.1123/ijspp.2021-0428
7. Fuller et al. (2020) — DOI: 10.2196/18694 *(nota: salvo localmente sob chave 10.2196/36780 — ver DEC-007)*

**Justificativa:** Todos tratam da relação entre exercício físico e tecnologias digitais (wearables, sensores, algoritmos), publicados entre 2018–2022, com texto completo disponível e DOI identificável. Atendem aos critérios de inclusão definidos em `01_METODOLOGIA.md`.

---

### [DEC-007] AUDITORIA | 2026-05-13

**Decisão:** Registrar **inconsistência de DOI** detectada no fichamento de Fuller et al. (2020).

**Problema identificado:** O arquivo `2023-JMIR-10.2196_36780.md` referencia o artigo de Fuller et al. (2020) com DOI real `10.2196/18694`, mas foi salvo localmente sob a chave `10.2196/36780`. Isso gera risco de confusão na citação.

**Ação corretiva:** O fichamento refeito (DEC-006) usará o DOI correto `10.2196/18694` como nome de arquivo e chave primária.

**Impacto:** O `AUDIT_LOG.json` deverá ser atualizado para refletir a correção.

---

*Próximas entradas serão adicionadas à medida que novos artigos forem fichados.*
