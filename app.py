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

aba_geral, aba_indicadores = st.tabs(
    ["Análise Geral de Listagens", "Indicadores Chave"]
)

with aba_geral:
    st.subheader("Distribuição e correlação")

    colunas_numericas = [
        coluna
        for coluna in VARS_QUANT
        if coluna in df_filtrado.columns
        and pd.api.types.is_numeric_dtype(df_filtrado[coluna])
    ]
    if colunas_numericas:
        variavel = st.selectbox("Variável para visualizar a distribuição", colunas_numericas)
        grafico_distribuicao = px.histogram(
            df_filtrado,
            x=variavel,
            title=f"Distribuição de {variavel}",
        )
        st.plotly_chart(grafico_distribuicao, width="stretch")
    else:
        st.info("Não há colunas numéricas disponíveis com os filtros atuais.")

    if {"room type", "price"}.issubset(df_filtrado.columns):
        # [IA] Plotly Express – Sintaxe do gráfico de boxplot
        grafico_boxplot = px.box(
            df_filtrado,
            x="room type",
            y="price",
            title="Price por room type",
        )
        st.plotly_chart(grafico_boxplot, width="stretch")
    else:
        st.info("As colunas 'room type' e 'price' são necessárias para exibir o boxplot.")

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
    st.subheader("Indicadores Chave")
    st.info("Espaço reservado para os cartões de KPIs que você definirá.")
