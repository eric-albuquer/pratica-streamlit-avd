# [IA] Copilot – Esqueleto inicial do app.py
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Dashboard Airbnb", layout="wide")

DATA_PATH = Path(__file__).parent / "Airbnb_Open_Data.csv"
VARS_QUANT = [
    "lat",
    "long",
    "Construction year",
    "price",
    "service fee",
    "minimum nights",
    "number of reviews",
    "reviews per month",
    "review rate number",
    "calculated host listings count",
    "availability 365",
]


@st.cache_data
def carregar_dados(caminho: str) -> pd.DataFrame:
    df = pd.read_csv(caminho, low_memory=False)

    for coluna in ("price", "service fee"):
        if coluna in df.columns:
            valores = df[coluna].astype("string").str.replace(r"[$,]", "", regex=True)
            df[coluna] = pd.to_numeric(valores, errors="coerce")

    df = df.drop(columns=["house_rules", "license"], errors="ignore")

    colunas_quant_presentes = [coluna for coluna in VARS_QUANT if coluna in df.columns]
    colunas_para_remover_nulos = [
        coluna
        for coluna in colunas_quant_presentes
        if coluna != "reviews per month" and df[coluna].isna().any()
    ]
    if colunas_para_remover_nulos:
        df = df.dropna(subset=colunas_para_remover_nulos).reset_index(drop=True)

    if "minimum nights" in df.columns and not df["minimum nights"].empty:
        q1, q3 = df["minimum nights"].quantile([0.25, 0.75])
        limite_superior = q3 + 1.5 * (q3 - q1)
        df = df[df["minimum nights"] <= limite_superior].reset_index(drop=True)

    if "price" in df.columns:
        df["price_log"] = np.log1p(df["price"])

    return df


st.title("Dashboard Airbnb — Nova York")

if not DATA_PATH.is_file():
    st.error(
        f"Arquivo não encontrado: {DATA_PATH.name}. "
        "Coloque o CSV na mesma pasta deste app.py."
    )
    st.stop()

df = carregar_dados(str(DATA_PATH))

if "neighbourhood group" not in df.columns or "price" not in df.columns:
    st.error("O CSV precisa conter as colunas 'neighbourhood group' e 'price'.")
    st.stop()

st.sidebar.header("Filtros")

grupos = sorted(df["neighbourhood group"].dropna().astype(str).unique().tolist())
grupos_selecionados = st.sidebar.multiselect(
    "Neighbourhood group",
    options=grupos,
    default=grupos,
)

precos_validos = df["price"].dropna()
if precos_validos.empty:
    st.sidebar.info("Não há valores válidos em 'price' para filtrar.")
    df_filtrado = df[df["neighbourhood group"].astype("string").isin(grupos_selecionados)]
else:
    preco_min = float(precos_validos.min())
    preco_max = float(precos_validos.max())

    if preco_min < preco_max:
        intervalo_preco = st.sidebar.slider(
            "Intervalo de price",
            min_value=preco_min,
            max_value=preco_max,
            value=(preco_min, preco_max),
        )
        filtro_preco = df["price"].between(*intervalo_preco)
    else:
        st.sidebar.caption(f"Valor disponível em price: {preco_min:g}")
        filtro_preco = df["price"].eq(preco_min)

    filtro_grupo = df["neighbourhood group"].astype("string").isin(grupos_selecionados)
    df_filtrado = df[filtro_grupo & filtro_preco]

colunas_numericas = [
    coluna
    for coluna in VARS_QUANT
    if coluna in df_filtrado.columns
    and pd.api.types.is_numeric_dtype(df_filtrado[coluna])
]
if colunas_numericas:
    variavel_selecionada = st.sidebar.selectbox(
        "Variável quantitativa",
        colunas_numericas,
    )

aba_geral, aba_indicadores = st.tabs(
    ["Análise Geral de Listagens", "Indicadores Chave"]
)

with aba_geral:
    st.subheader("Distribuição e correlação")

    if colunas_numericas:
        # [IA] Plotly – Histograma de Distribuição de Preços
        fig_histograma = px.histogram(
            df_filtrado,
            x="price",
            nbins=30,
            labels={"price": "Price (US$)"},
        )
        mediana_preco = df_filtrado["price"].dropna().median()
        if pd.notna(mediana_preco):
            fig_histograma.add_vline(
                x=mediana_preco,
                line_dash="dash",
                annotation_text=f"Mediana: {mediana_preco:.2f}",
            )
        st.plotly_chart(fig_histograma, width="stretch")

        grafico_variavel = px.histogram(
            df_filtrado,
            x=variavel_selecionada,
            title=f"Distribuição de {variavel_selecionada}",
        )
        st.plotly_chart(grafico_variavel, width="stretch")
    else:
        st.info("Não há colunas numéricas disponíveis com os filtros atuais.")

    if {"neighbourhood group", "price"}.issubset(df_filtrado.columns):
        # [IA] Plotly – Boxplot de Preço por Distrito
        fig_boxplot = px.box(
            df_filtrado,
            x="neighbourhood group",
            y="price",
            range_y=[0, 1200],
            labels={
                "neighbourhood group": "Neighbourhood group",
                "price": "Price (US$)",
            },
        )
        st.plotly_chart(fig_boxplot, width="stretch")
    else:
        st.info(
            "As colunas 'neighbourhood group' e 'price' são necessárias para exibir o boxplot."
        )

    if len(colunas_numericas) >= 2:
        correlacao = df_filtrado[colunas_numericas].corr(method="spearman")
        grafico_correlacao = px.imshow(
            correlacao,
            aspect="auto",
            color_continuous_scale="RdBu",
            zmin=-1,
            zmax=1,
            title="Correlação de Spearman entre variáveis quantitativas",
        )
        st.plotly_chart(grafico_correlacao, width="stretch")
    else:
        st.info("São necessárias ao menos duas colunas numéricas para exibir a correlação.")

with aba_indicadores:
    # [IA] Streamlit & Plotly – Implementação de KPIs e Visuais de Precificação e Mercado
    st.subheader("Visão de Precificação e Mercado")

    colunas_kpi = st.columns(3)
    metricas = (
        ("Preço Médio por Noite", "price", "mean"),
        ("Mediana de Preço", "price", "median"),
        ("Taxa de Serviço Média", "service fee", "mean"),
    )

    for coluna_kpi, (titulo, coluna, calculo) in zip(colunas_kpi, metricas):
        if coluna in df_filtrado.columns:
            serie = df_filtrado[coluna].dropna()
            valor = getattr(serie, calculo)() if not serie.empty else float("nan")
            valor_formatado = f"R$ {valor:,.2f}" if pd.notna(valor) else "—"
        else:
            valor_formatado = "—"
        coluna_kpi.metric(titulo, valor_formatado)

    if {"neighbourhood group", "price"}.issubset(df_filtrado.columns):
        fig_boxplot_precos = px.box(
            df_filtrado,
            x="neighbourhood group",
            y="price",
            range_y=[0, 1200],
        )
        st.plotly_chart(fig_boxplot_precos, width="stretch")

    if "price" in df_filtrado.columns:
        fig_histograma_precos = px.histogram(
            df_filtrado,
            x="price",
            nbins=30,
        )
        mediana_preco = df_filtrado["price"].dropna().median()
        if pd.notna(mediana_preco):
            fig_histograma_precos.add_vline(
                x=mediana_preco,
                line_dash="dash",
                annotation_text=f"Mediana: {mediana_preco:.2f}",
            )
        st.plotly_chart(fig_histograma_precos, width="stretch")
