# Metodologia — Revisão Integrativa
**Documento:** 01 — Metodologia  
**Versão:** 1.0 — DRAFT  
**Referência-base:** Mendes, Silveira e Galvão (2008). *Revisão integrativa: método de pesquisa para a incorporação de evidências na saúde e na enfermagem.* Texto Contexto Enferm, 17(4): 758–64.

---

## 1. Etapa 1 — Elaboração da Pergunta Norteadora

A pergunta norteadora foi estruturada com foco no **mapeamento do campo**, não na avaliação de eficácia de intervenções:

> *O que se tem produzido academicamente acerca da relação entre exercício físico e tecnologias digitais no período de 2018 a 2026, sobretudo no que se refere às principais áreas e assuntos investigados?*

**Posicionamento metodológico:**  
Este estudo constitui uma **atualização e extensão** da revisão de Oliveira et al. (2020), que cobriu o período 2013–2018 nas bases SPORTDiscus e Google Scholar. A presente revisão expande o período (2018–2026) e amplia as bases de busca para capturar a produção internacional mais recente, especialmente em periódicos de saúde digital.

---

## 2. Etapa 2 — Busca na Literatura

### 2.1 Bases de Dados
| Base | Justificativa |
|---|---|
| PubMed / NCBI | Base de dados biomédica de referência global; cobre JMIR, BMJ, Lancet Digital Health |
| JMIR Publications | Especializada em saúde digital e mHealth; maior volume de artigos sobre apps e wearables |
| Scopus | Cobertura multidisciplinar; indexa periódicos de Educação Física, Ciências do Esporte e Tecnologia |

### 2.2 Estratégia de Busca (Descritores)

Cruzamento via operador booleano AND entre dois conjuntos de termos:

**Conjunto A — Exercício Físico:**
`"physical exercise" OR "physical activity" OR "exercise" OR "sport" OR "fitness" OR "rehabilitation"`

**Conjunto B — Tecnologias Digitais:**
`"digital technology" OR "wearable" OR "mobile app" OR "mHealth" OR "smartphone" OR "gamification" OR "machine learning" OR "artificial intelligence" OR "telehealth" OR "exergame"`

### 2.3 Filtros Aplicados
- **Período:** Janeiro de 2018 a Dezembro de 2026
- **Idioma:** Inglês (língua primária); Português (complementar)
- **Tipo de acesso:** Preferencialmente Open Access (Free Full Text)
- **Tipos de estudo incluídos:** Ensaios clínicos randomizados, revisões sistemáticas, meta-análises, estudos de viabilidade, estudos transversais, estudos qualitativos

---

## 3. Etapa 3 — Critérios de Inclusão e Exclusão

### Critérios de Inclusão
- Estudos que abordam a relação entre **prática de exercícios físicos** e **tecnologias digitais**
- Publicados entre **2018 e 2026**
- Disponíveis em **inglês ou português**
- Com **texto completo disponível**
- Com **DOI identificável** (garantia de rastreabilidade)

### Critérios de Exclusão
- Estudos cuja ênfase está em **marketing esportivo** ou **gestão empresarial** de clubes
- Estudos sobre **práticas de animais** (adestramento etc.)
- Estudos que tratam exclusivamente de **mídias tradicionais** (TV, rádio) sem componente digital interativo
- **Editoriais, cartas ao editor e comentários** sem dados primários
- Estudos com **metodologia insuficientemente descrita**

---

## 4. Etapa 4 — Coleta de Dados (Fichamento)

Cada artigo incluído é processado segundo o **Template Canônico de Fichamento Acadêmico** (ver documento `TEMPLATE_FICHAMENTO.md`), que extrai:
1. Identificação completa (autores, ano, DOI, revista)
2. Objetivo do estudo
3. Delineamento metodológico
4. Tecnologia(s) investigada(s)
5. População estudada
6. Principais achados (descritivo, não interpretativo)
7. Limitações reportadas pelos autores
8. Classificação provisória de categoria temática

**Auditoria de integridade:** Todos os PDFs são identificados por DOI como chave primária e registrados no `AUDIT_LOG.json` com hash SHA-256.

---

## 5. Etapa 5 — Análise Crítica e Categorização

### 5.1 Abordagem
A categorização segue método **indutivo**: as categorias **emergem da leitura** dos artigos, não são pré-definidas. O processo segue o modelo de Oliveira et al. (2020):
1. Leitura flutuante dos fichamentos
2. Identificação de temáticas recorrentes
3. Agrupamento por similaridade temática
4. Nomeação das categorias
5. Validação das categorias pelo conselho científico

### 5.2 Registro de Decisões
Cada decisão de inclusão/exclusão e cada decisão de categorização é registrada no documento `02_REASONING_LOG.md` com justificativa explícita.

---

## 6. Etapa 6 — Apresentação da Revisão

O artigo final seguirá a estrutura do artigo modelo (Oliveira et al., 2020):
1. Introdução
2. Método
3. Resultados e Discussão (organizado por categorias emergentes)
4. Considerações Finais

O **Fluxograma PRISMA** (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) será incluído para transparência do processo de seleção, conforme exigência crescente dos periódicos internacionais.

---

> [!NOTE]
> O PRISMA foi originalmente desenvolvido para revisões sistemáticas, mas seu fluxograma de seleção é amplamente adotado em revisões integrativas para demonstrar transparência metodológica. Seu uso aqui não transforma o estudo em revisão sistemática.
