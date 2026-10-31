# Dashboard Airbnb — Nova York

Aplicação acadêmica em Streamlit baseada no Airbnb Open Data, com uma aba de análise geral e uma aba de indicadores.

**Repositório:** [eric-albuquer/pratica-streamlit-avd](https://github.com/eric-albuquer/pratica-streamlit-avd)

## Aplicação publicada

**Status:** ainda não publicada. Após o deploy, substitua esta linha pela URL pública do app.

## Executar localmente

Na pasta do projeto, instale as dependências e inicie o Streamlit:

```powershell
python -m pip install streamlit pandas numpy plotly
python -m streamlit run app.py
```

O arquivo `Airbnb_Open_Data.csv` deve ficar na mesma pasta que `app.py`.

## Estrutura

- `app.py`: aplicação Streamlit.
- `eda.ipynb`: notebook de análise exploratória.
- `entregas/`: rascunhos dos dois dashboards e espaço para justificar individualmente as métricas.
- `prompts/`: declaração de uso de IA e registro dos usos.

## Verificações antes da entrega

- [ ] Publicar o app e inserir a URL acima.
- [ ] Abrir o app publicado em janela anônima.
- [ ] Interagir com os filtros e o seletor de variável.
- [ ] Confirmar que as duas abas e seus gráficos carregam.
- [ ] Confirmar que a interface não expõe dados sensíveis.
- [ ] Completar a justificativa individual das métricas em `entregas/justificativa-metricas.md`.
- [ ] Revisar, assinar e entregar a declaração de uso de IA em PDF.
