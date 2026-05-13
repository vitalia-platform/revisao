# Relatório de Raciocínio (Reasoning) e Auditoria do Corpus
**Projeto:** Plataforma Vitalia — Revisão Integrativa da Literatura
**Data:** Maio de 2026
**Responsável:** Equipe de Ciência e Engenharia Vitalia

---

## 1. OBJETIVO DO RELATÓRIO
Este documento detalha o processo lógico de construção do conhecimento (reasoning) que alicerça o rascunho do artigo final, bem como a trilha de auditoria metodológica que assegura a integridade dos dados e protege o projeto de Vieses de Confirmação e Alucinações Acadêmicas.

## 2. METODOLOGIA DE SELEÇÃO E AUDITORIA
O corpus bibliográfico foi extraído mediante curadoria algorítmica e humana, submetido ao rigor metodológico PRISMA 2020. A construção do acervo baseou-se em três princípios fundamentais de engenharia de software aplicados à ciência:

### 2.1. Funil de Triagem (PRISMA)
- **Identificação Inicial:** 1.250 artigos provenientes das principais bases de dados (PubMed, JMIR, Scopus).
- **Remoção de Ruído:** Exclusão de 150 duplicatas, além de 980 artigos fora do escopo através de triagem ágil (exclusões baseadas em testes em animais, marketing e metodologias falhas).
- **Leitura Integral:** 120 artigos passaram para a fase de "Full-Text Review". Destes, 89 foram descartados para refinar a densidade clínica do material (exclusão por falta de dados primários e ausência de identificadores DOI ativos).
- **Corpus Final:** 31 artigos selecionados, lidos, fichados e validados.

### 2.2. Trilha de Auditoria Anti-Fraude
Para garantir que os extratos biomédicos que alimentarão os "Motores Vitalia" sejam inquestionáveis, implementou-se:
1. **Hashing Criptográfico (SHA-256):** Todos os 31 PDFs originais foram submetidos a um hash assimétricos e congelados localmente (`/docs-analise/artigo-revisao/artigos/`). Isso impossibilita adulterações pós-fichamento.
2. **DOI como Chave Primária:** Nenhum artigo foi admitido sem um DOI verificável, rejeitando *preprints* não validados ou URLs não rastreáveis.

## 3. RACIOCÍNIO (REASONING) DA SÍNTESE
O raciocínio para a síntese teórica focou em abandonar o discurso marqueteiro de "tecnologia mágica" e extrair o *estado clínico real* dos dispositivos. Identificamos as três teses centrais da Vitalia:

**A. Dose-Efeito Tecnológica (Foco em Capilaridade)**
Decidimos incluir meta-análises de países de baixa e média renda (ex: Boima et al., 2024). O raciocínio é provar que a interface primária (mesmo sendo um simples SMS) possui valor clínico para controle pressórico comparável a intervenções complexas. A tecnologia importa pela "frequência do contato", não pelo preço da tela.

**B. O Paradoxo da Adesão (Por que apps falham)**
Ao invés de apenas confirmar que "apps funcionam", procuramos intencionalmente na literatura os motivos de abandono. O achado de Kassavou et al. (2022) foi crítico: *automonitoramento isolado reduz a pressão em pífios -0.72 mmHg, mas se acoplado a feedback humano (tailored advice) a redução é de -2.92 mmHg*. Raciocínio aplicado: Vitalia não será apenas um painel de dados, será uma plataforma de feedback ativo (Motor Keytel).

**C. A Acurácia no Mundo Real**
Excluímos testes de esteira perfeitos (laboratoriais) para focar no "Free-Living". Singh et al. (2024) comprovaram que a fibrilação atrial é identificada com maestria (95% especificidade) por Apple Watches e Fitbits, mas a detecção de quedas falha com altas taxas de falsos positivos (62% especificidade). Raciocínio aplicado: Vitalia absorverá *apenas* a telemetria cardíaca validada, mantendo máxima cautela com promessas de predição motora de sensores de pulso.

## 4. CONCLUSÃO DA AUDITORIA
Os 31 fichamentos originais garantem a proveniência dos dados. O *Reasoning* construído permite à equipe avançar de forma segura para o desenvolvimento da engenharia de *software* biomédica, sabendo que os Motores da plataforma respeitarão as delimitações estritas da ciência atual.

> **Status:** ✅ Validado para apresentação em Conselho.
