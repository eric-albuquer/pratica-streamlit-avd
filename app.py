# [IA] Copilot – Esqueleto inicial do app.py
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Dashboard Airbnb", layout="wide")

DATA_PATH = Path(__file__).parent / "Airbnb_Open_Data.csv"


@st.cache_data
def carregar_dados(caminho: str) -> pd.DataFrame:
    df = pd.read_csv(caminho, low_memory=False)
    if "price" in df.columns:
        preco = df["price"].astype("string").str.replace(r"[$,]", "", regex=True)
        df["price"] = pd.to_numeric(preco, errors="coerce")
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

    colunas_numericas = df_filtrado.select_dtypes(include="number").columns.tolist()
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

    if len(colunas_numericas) >= 2:
        correlacao = df_filtrado[colunas_numericas].corr()
        grafico_correlacao = px.imshow(
            correlacao,
            aspect="auto",
            color_continuous_scale="RdBu",
            zmin=-1,
            zmax=1,
            title="Correlação entre variáveis numéricas",
        )
        st.plotly_chart(grafico_correlacao, width="stretch")
    else:
        st.info("São necessárias ao menos duas colunas numéricas para exibir a correlação.")

with aba_indicadores:
    st.subheader("Indicadores Chave")
    st.info("Espaço reservado para os cartões de KPIs que você definirá.")
