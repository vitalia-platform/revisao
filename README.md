# Revisão Integrativa: Tecnologias Digitais no Exercício Físico (2018–2026)

Este repositório contém o protocolo, a base de dados e os artefatos da revisão integrativa da literatura realizada para fundamentar o motor fisiológico **Kim/Keytel** da plataforma Vitalia.

---

## 1. Objetivo e Escopo
O objetivo desta revisão é sintetizar evidências científicas sobre o impacto de tecnologias digitais (Wearables, IA, mHealth e Gamificação) na promoção da atividade física, adesão ao exercício e monitoramento de biomarcadores.

- **Pergunta de Pesquisa (PCC):** Como as tecnologias digitais de 3ª geração influenciam o comportamento de exercício e a precisão do monitoramento fisiológico em diversas populações?
- **Período:** 2018 – 2026.
- **Base de Dados:** PubMed, PMC, JMIR, Frontiers, BMJ.

---

## 2. Metodologia (6 Etapas)
Seguimos o rigor metodológico da Revisão Integrativa:

1.  **Identificação do Tema:** Foco em convergência tecnológica e saúde digital.
2.  **Busca na Literatura:** Critérios de inclusão baseados em DOIs permanentes e Open Access.
3.  **Categorização:** Organização por 10 eixos temáticos (Wearables, IA, VR, etc.).
4.  **Avaliação Crítica:** Uso de critérios de qualidade JMIR 2024.
5.  **Interpretação dos Resultados:** Extração de parâmetros para o motor Kim/Keytel.
6.  **Síntese do Conhecimento:** Consolidação em diretrizes de código e HITL Médico.

---

## 3. Auditoria e Rastreabilidade
Para garantir a integridade científica e permitir auditoria posterior:

### Métodos de Auditoria
- **Identificador Único:** Cada artigo é indexado pelo seu **DOI** (Digital Object Identifier).
- **Integridade de Arquivo:** Todos os PDFs possuem hashes **SHA-256** registrados no [AUDIT_LOG.json](file:///Users/andre/projetos/assistidos/revisao/docs-analise/artigo-revisao/AUDIT_LOG.json).
- **Consistência de Nomenclatura:** Arquivos renomeados para o padrão `ANO - Autor - DOI_suffix.pdf`.

### Como Verificar
Para verificar a integridade da base local, execute:
```bash
shasum -a 256 -c docs-analise/artigo-revisao/AUDIT_LOG.json
```
*(Nota: O log deve ser convertido para o formato shasum se necessário, ou verificado via script python).*

---

## 4. Estrutura do Repositório
- `docs-analise/artigo-revisao/artigos/`: PDFs auditados e renomeados.
- `docs-analise/artigo-revisao/fichamentos/`: Análises técnicas individuais.
- `docs-analise/artigo-revisao/lista_links_manual.md`: Índice mestre por DOI.
- `docs-analise/artigo-revisao/AUDIT_LOG.json`: Metadados de auditoria.

---

## 5. Próximos Passos
- [ ] Concluir o fichamento técnico dos 31 artigos.
- [ ] Analisar material suplementar do Artigo 19 (Efeitos de Telehealth).
- [ ] Extrair constraints para o HITL Médico.

---
> [!IMPORTANT]
> **HITL Médico:** Todo conteúdo gerado por IA nesta revisão deve ser revisado por um profissional de saúde antes de ser implementado em produção.
