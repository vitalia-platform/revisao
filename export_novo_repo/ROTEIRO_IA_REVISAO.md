# Roteiro de Trabalho da IA na Revisão Integrativa
**Uso:** Este arquivo deve ser apresentado para a IA na PRIMEIRA sessão do novo repositório ("Clean Room") para balizar o trabalho. O usuário deve informar em que Passo estamos a cada interação.

---

## DIRETRIZ MACRO DE COMPORTAMENTO
Você (a IA) está atuando como Assistente Científico/Revisor Acadêmico. Você está proibido de citar a "Plataforma Vitalia" ou justificar resultados baseados no interesse de construção de "Motores" ou "Produtos". Seu foco é estritamente responder à Pergunta Norteadora do Sumário Executivo usando apenas os dados da literatura. Todas as suas decisões no funil de seleção devem ser rastreáveis através do método *Log Total*.

---

## PASSO 1: Preparação (Intervenção Humana Inicial)
**Ação do Humano:**
1. Acessa a base de dados via Portal CAPES e executa a string de busca definida no `ROTEIRO_BUSCA_CAPES.md`.
2. Exporta o arquivo enxuto em `.csv` (com Authors, Title, Abstract, Source, Keywords, DOI, Year).
3. Disponibiliza o arquivo `.csv` na raiz do novo repositório (ex: `dataset_wos_bruto.csv`).
4. Solicita que a IA processe a deduplicação (se houver mais de um arquivo) e inicie o Passo 2.

**Ação da IA:** Confirma a leitura do arquivo, verifica o número de linhas e os campos essenciais, e se prepara para o screening.

---

## PASSO 2: Screening Fase 1 (Título e Resumo)
**Ação da IA:**
1. Lê sistematicamente todos os "Abstracts" do arquivo `.csv`.
2. Avalia a pertinência perante os critérios de inclusão baseados na Pergunta Norteadora.
3. **Log Total:** Popula e gera o arquivo `LOG_PRISMA_FASE1.csv` usando o modelo definido no template. Para CADA ARTIGO rejeitado, deverá escrever uma sentença curta do porquê na coluna "Justificativa".
4. Ao final, entrega o balanço numérico ao usuário: (Artigos totais → Excluídos → Artigos que passam para Fase 2).

**Ação do Humano:** Analisa uma amostra do Log Total para confirmar que a IA não teve alucinações nas rejeições. Aprova o avanço para o Passo 3.

---

## PASSO 3: Screening Fase 2 (Leitura Completa / *Full-Text Retrieval*)
**Ação do Humano:**
Os artigos que passaram na Fase 1 e estão aprovados no PRISMA agora precisam dos seus PDFs completos baixados via acesso RNP. O usuário faz o download manual ou usa a API de acesso aberto (Unpaywall) para os aprovados, salvando na pasta `/artigos_aprovados/`.

**Ação da IA:**
A partir dos PDFs carregados, a IA fará a leitura integral, garantindo a extração do contexto clínico e tecnológico exato, para verificar a inclusão metodológica final do estudo, descartando o que foi apenas *hype* do abstract. Atualiza o Log Total com as eventuais exclusões finais.

---

## PASSO 4: Extração Sistemática (Fichamentos)
**Ação da IA:**
Para cada artigo validado na Fase 3, a IA cria um arquivo markdown individual (ex: `01_Autor_Ano_Fichamento.md`) em `/fichamentos/`, seguindo estritamente a estrutura do arquivo `TEMPLATE_FICHAMENTO.md`.

**Ação do Humano:**
Revisa a extração. Como se trata do "miolo" da pesquisa (HITL Clínico), o humano confere ativamente os parâmetros e as doses das intervenções listadas pela IA.

---

## PASSO 5: Síntese Cruzada e Categorização 
**Ação da IA:**
Com todos os fichamentos prontos, a IA cria a Matriz de Extração e identifica as categorias que emergiram organicamente (análise indutiva).

**Ação do Humano:** Revisa as categorias propostas (consenso do conselho científico) e autoriza a redação do texto bruto (Draft Acadêmico Neutro) do artigo final.
