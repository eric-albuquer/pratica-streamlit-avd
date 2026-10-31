# Rascunho do Dashboard 2 — Indicadores

## Público-alvo informado pelo estudante

Anfitriões e gestores de imóveis; investidores do mercado imobiliário; analistas de mercado e consultores de hospitality. O estudante definiu esses públicos e descreveu seus objetivos na conversa de apoio.

## Métricas selecionadas pelo estudante

1. Taxa de Serviço Média.
2. Disponibilidade Média.
3. Avaliações/Mês (Média).
4. Estadia Mínima Média.
5. Percentual de Reserva Imediata.

## Esboço

```text
┌──────────────────────────────────────────────────────────────────────┐
│ DASHBOARD 2 — INDICADORES                                            │
│ Público-alvo: anfitriões/gestores, investidores e analistas          │
├──────────────────┬──────────────────┬──────────────────┬────────────┤
│ Disponibilidade  │ Avaliações/mês   │ Estadia mínima   │ Reserva    │
│ média            │ média            │ média            │ imediata   │
├──────────────────────────────────────────────────────────────────────┤
│ Taxa de Serviço Média                                                 │
├────────────────────────────────┬─────────────────────────────────────┤
│ Boxplot: price por distrito     │ Histograma de price + mediana      │
├────────────────────────────────┼─────────────────────────────────────┤
│ Dispersão: disponibilidade x   │ Barras: média de dias disponíveis  │
│ avaliações, cor por room type  │ por distrito                        │
└────────────────────────────────┴─────────────────────────────────────┘
```

## Visuais previstos

- Boxplot de `price` por `neighbourhood group`, com eixo visual até 1.200.
- Histograma de `price` com 30 bins e linha da mediana.
- Dispersão de `availability 365` por `number of reviews`, colorida por `room type`.
- Barras da média de `availability 365` por `neighbourhood group`.

Todos os componentes dependem de `df_filtrado`. A justificativa individual para cada métrica deve ser preenchida em [justificativa-metricas.md](./justificativa-metricas.md), com base na EDA e no público-alvo escolhido pelo estudante.
