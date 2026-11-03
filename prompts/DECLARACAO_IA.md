# **1\. Identificação**

| Campo | Informação |
|---|---|
| Turma | ☒ 5A　☐ 5B |
| Nome completo | Eric Gonçalves Albuquerque |
| E-mail | ega2@cesar.school |
| Repositório | https://github.com/eric-albuquer/pratica-streamlit-avd |
| Data de entrega | 01/11/2026 |

# **2\. Diretrizes (leiam antes de usar qualquer ferramenta)**

**Permitido, desde que registrado na Seção 5:**

> * Usar a Skill oficial do Streamlit (streamlit skills) para orientar a IA a gerar código no padrão correto da biblioteca.

> * Gerar o esqueleto do app.py a partir do seu rascunho de layout, usando o Template de Prompt (Contexto, Entrada, Restrições, Formato de saída). Essa etapa faz parte da própria atividade (Aula 21).

> * Apoio na criação de identidade visual e/ou apoio na otimização da interface do dashboard.

> * Tirar dúvidas conceituais sobre Streamlit, Python, pandas, Git etc., como um tutor.

> * Apoio com a sintaxe de bibliotecas de visualização (Altair, Plotly, Seaborn, matplotlib): o código que desenha o gráfico, não a escolha do gráfico nem a interpretação dele.

> * Entender mensagens de erro e depurar código (local ou do deploy).

> * Revisar a ortografia e clareza do README e de textos escritos por você.

**Proibido:**

> * Deixar que a IA escolha, proponha ou justifique sozinha as métricas do Dashboard 2\. As métricas podem ser calculadas com apoio de IA, mas a escolha de quais usar e por quê precisa ser sua, validada individualmente e consistente com o que você escreveu em entregas/justificativa-metricas.md.

> * Pedir que a IA interprete os dados, escreva a justificativa das métricas ou tire conclusões sobre o seu dataset em seu lugar.

> * Entregar qualquer trecho de código que você não saiba explicar. Inclusive o esqueleto do app.py gerado via IA/Skill.

> * Omitir o uso de IA ou da Skill do Streamlit.

**Obrigatório:**

> * Declarar se usou ou não a Skill oficial do Streamlit (streamlit skills)  

> * obrigatório mesmo que o único uso de IA tenha sido gerar o esqueleto do app.py com ela.

> * Entregar esta declaração preenchida e assinada, mesmo que você não tenha usado IA.

> * Marcar no código todo trecho feito com apoio de IA: \# \[IA\] \<ferramenta\> – \<finalidade\>.

> * Registrar cada uso na Seção 5 OU compartilhar os links (ou arquivos) das conversas completas com a professora (única forma de dispensar o registro bloco a bloco)

| Situação | Consequência |
| :---- | :---- |
| Uso declarado e dentro das diretrizes | Sem desconto. |
| Uso proibido, porém declarado | Itens afetados avaliados como “Não entregue”. |
| Uso não declarado, ou código/análise que você não sabe explicar | Nota ZERO no projeto. |
| Declaração ausente ou sem assinatura | Nota ZERO no projeto. |

Na dúvida sobre se um uso é permitido, pergunte à professora **antes** de usar.

# **3\. Declaração geral (marque uma opção)**

☐ **Não utilizei** nenhuma ferramenta de IA generativa em nenhuma etapa do projeto.

☒ **Utilizei** IA generativa e registrei os usos abaixo. A Skill oficial do Streamlit não foi utilizada nesta sessão.
# **4\. Ferramentas utilizadas**

| Ferramenta | Versão / plano | Parte da atividade |
|---|---|---|
| Copilot via SDK no VS Code | Versão/plano não identificado nesta sessão | Esqueleto e alterações do `app.py`, sintaxe Streamlit/Plotly, depuração, revisão de requisitos e estrutura de entregáveis |
# **5\. Registro de usos**

**Forma escolhida: Opção B — registro bloco a bloco.** Os registros abaixo resumem os pedidos desta conversa; não são uma transcrição integral. O estudante deve conferir o histórico completo antes de assinar. A Skill oficial do Streamlit não foi utilizada.

| Uso / data | Parte e finalidade permitida | Pedido resumido | O que foi aproveitado / modificado | Verificação |
|---|---|---|---|---|
| 1 — 30/10/2026 | `app.py`; esqueleto a partir do layout fornecido | Montar estrutura Streamlit com filtros, abas, cache, histogramas e correlação. | Esqueleto inicial adaptado ao layout solicitado. | `py_compile`; inspeção do arquivo. |
| 2 — 30/10/2026 | `app.py`; depuração | Explicar avisos de execução fora do runtime Streamlit e avisos de Pandas/Streamlit. | Orientação de execução com `streamlit run`; leitura com `low_memory=False` e parâmetro de largura atualizado. | `py_compile`; execução de teste Streamlit. |
| 3 — 31/10/2026 | `app.py`; sintaxe de gráfico Plotly | Sintaxe de boxplot e aplicação no app; depois histograma e boxplot por distrito com eixo visual limitado. | Gráficos conforme especificações fornecidas pelo estudante. | `py_compile` e `AppTest`. |
| 4 — 31/10/2026 | `app.py`; tratamento com Pandas e correlação | Conferir a EDA e reproduzir conversão de preços, remoção de colunas, tratamento de nulos e correlação. | Tratamentos observados no notebook; correlação Spearman sobre variáveis quantitativas listadas. | Conferência do notebook, `py_compile` e `AppTest`. |
| 5 — 31/10/2026 | `app.py`; limpeza de dados | Remover extremos em `minimum nights`. | Aplicação do limite superior pela regra IQR. | Checagem do limite no CSV, `py_compile` e `AppTest`. |
| 6 — 31/10/2026 | `app.py`/requisitos; revisão técnica | Comparar a aplicação ao `requisitos.txt` e identificar itens pendentes sem escolher métricas. | Lista de pendências; decisão de métricas solicitada ao estudante. | Comparação direta com `requisitos.txt`. |
| 7 — 31/10/2026 | Dashboard 2; sintaxe Streamlit/Plotly | Implementar cartões e visuais de precificação e disponibilidade; a IA também sugeriu métricas candidatas. | O estudante analisou as sugestões junto aos dados, descartou as métricas que apresentavam valores muito próximos e escolheu as cinco métricas finais. | `py_compile`, `AppTest` e análise dos valores no dataset. |
| 8 — 31/10/2026 | `entregas/`, `prompts/`, README e declaração | Completar os arquivos exigidos e adequar o número de métricas ao requisito. | Estruturas de rascunhos/README/registro; público-alvo e cinco métricas fornecidos pelo estudante; justificativas pessoais ficaram para preenchimento individual. | Revisão do diff e testes locais. |
# **6\. Trechos de código feitos com apoio de IA**

| Arquivo / parte | Teve apoio de IA? | Tipo de apoio |
|---|---|---|
| `app.py` (esqueleto e tratamentos) | ☒ Sim ☐ Não | Estrutura inicial, sintaxe Streamlit/Pandas e depuração. |
| Dashboard 1 (correlação e distribuição) | ☒ Sim ☐ Não | Sintaxe dos gráficos e integração com filtros. |
| Dashboard 2 (KPIs e visuais) | ☒ Sim ☐ Não | Implementação das métricas e gráficos escolhidos/especificados pelo estudante. |
| Deploy / configuração | ☐ Sim ☒ Não | O app ainda não foi publicado. |
| Skill oficial do Streamlit | ☐ Sim ☒ Não | Não utilizada nesta sessão. |
# **7\. Reflexão individual (8 a 15 linhas)**

**PREENCHIMENTO INDIVIDUAL OBRIGATÓRIO — revise e ajuste o texto para confirmar que representa sua experiência antes de assinar.** Texto organizado a partir dos pontos relatados pelo estudante.

1. A IA me ajudou bastante a acelerar o desenvolvimento do aplicativo em Streamlit.
2. Mesmo sem conhecer a sintaxe do framework, consegui avançar na construção do app com esse apoio.
3. Usei prompts para descrever como imaginava os dashboards e transformar essas ideias em telas e visualizações.
4. A IA também sugeriu algumas métricas que poderiam ser incluídas no Dashboard 2.
5. Analisei os dados antes de decidir quais sugestões seriam realmente úteis para o meu projeto.
6. Percebi que algumas métricas apresentavam valores muito próximos entre si.
7. Por isso, considerei que incluí-las não acrescentaria informação relevante aos dashboards e optei por descartá-las.
8. A escolha final das métricas foi minha, com base na análise dos dados e nos objetivos do dashboard; usei a IA como apoio, não como substituta da minha avaliação.
# **8\. Termo de responsabilidade**

**PENDENTE:** leia e confirme o termo abaixo. Assine somente depois de completar a reflexão e verificar que todas as declarações são verdadeiras.

Declaro que as informações deste documento são verdadeiras e completas; que compreendo e sei explicar todo o código, as saídas e as análises entregues, inclusive os trechos feitos com apoio de IA; e que estou ciente das consequências descritas na Seção 2.

| Nome | Assinatura (manuscrita ou gov.br) | Data da assinatura |
|---|---|---|
| Eric Gonçalves Albuquerque | **[ASSINATURA DO ESTUDANTE PENDENTE]** | **[PREENCHER]** |
