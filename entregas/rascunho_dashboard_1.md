# Rascunho do Dashboard 1 — Análise Geral de Listagens

## Objetivo de layout

Laboratório interativo para visualizar distribuições e correlações com os filtros selecionados.

## Esboço

```text
┌───────────────────────┐  ┌──────────────────────────────────────────────┐
│ SIDEBAR               │  │ ANÁLISE GERAL DE LISTAGENS                   │
│                       │  │                                              │
│ neighbourhood group   │  │ Histograma de price (30 bins + mediana)      │
│ [multiselect]         │  │                                              │
│                       │  │ Histograma da variável selecionada           │
│ Intervalo de price    │  │                                              │
│ [slider]              │  │ Boxplot de price por neighbourhood group     │
│                       │  │ (eixo Y até 1.200)                            │
│ Variável quantitativa │  │                                              │
│ [selectbox]           │  │ Mapa de calor de correlação de Spearman       │
└───────────────────────┘  └──────────────────────────────────────────────┘
```

## Componentes previstos

- Filtro multiselect por `neighbourhood group`.
- Slider de intervalo de `price`.
- Seletor de variável quantitativa para o histograma.
- Histograma de `price` com linha de mediana.
- Histograma da variável selecionada.
- Boxplot de `price` por distrito.
- Mapa de calor com correlação de Spearman.

Os gráficos usam o DataFrame filtrado. Este documento descreve a estrutura visual, sem interpretação dos resultados.
