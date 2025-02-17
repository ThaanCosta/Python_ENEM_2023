import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config.db_config import database_config

from queries.queries import (
    QUERY_TOTAL_INSCRITOS, QUERY_TOTAL_TREINEIROS_SIM, QUERY_TOTAL_TREINEIROS_NAO,
    QUERY_TOP5_FAIXA_RENDA, QUERY_TOP5_QTDE_ALUNOS_UF, QUERY_TIPO_ESCOLA
)

# Configuração do estilo dos gráficos
plt.style.use("dark_background")

# Construa a string de conexão corretamente formatada
connection_string = URL.create(
    "mssql+pyodbc",
    username=database_config['username'],
    password=database_config['password'],
    host=database_config['host'],
    database=database_config['database'],
    query={"driver": "ODBC Driver 17 for SQL Server"}
)

# Criar o engine do SQLAlchemy
engine = create_engine(connection_string, echo=True, fast_executemany=True)

# Criar menu lateral
st.sidebar.title("📊 Opções de Visualização")
menu_option = st.sidebar.radio(
    "Selecione uma análise:",
    ["📈 Inscrições", "💰 Faixa de Renda", "🌎 Estados", "🏫 Tipo de Escola"]
)

# Função para buscar dados
def get_data(query):
    conn = engine.raw_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Buscar dados

dfTotalInscritos = get_data(QUERY_TOTAL_INSCRITOS)
dfTotalTreineirosSim = get_data(QUERY_TOTAL_TREINEIROS_SIM)
dfTotalTreineirosNao = get_data(QUERY_TOTAL_TREINEIROS_NAO)
dfTop5FaixaDeRenda = get_data(QUERY_TOP5_FAIXA_RENDA)
dfTop5QtdeAlunosPorUF = get_data(QUERY_TOP5_QTDE_ALUNOS_UF)
dfTipoEscola = get_data(QUERY_TIPO_ESCOLA)

# Formatar valores dos KPIs
formatted_total_inscritos = f"{dfTotalInscritos['TotalInscritos'][0]:,}".replace(',', '.')
formatted_total_treineiro_sim = f"{dfTotalTreineirosSim['Sim_Treineiro'][0]:,}".replace(',', '.')
formatted_total_treineiro_nao = f"{dfTotalTreineirosNao['Nao_Treineiro'][0]:,}".replace(',', '.')

# Título principal
st.markdown("<h1 style='text-align: center; color: white;'>📊 ANALYTICS ENEM - 2023</h1>", unsafe_allow_html=True)

# KPIs
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.metric(label="📌 **Total de Inscritos**", value=formatted_total_inscritos)
with col2:
    st.metric(label="🎯 **Total Treineiros**", value=formatted_total_treineiro_sim)
with col3:
    st.metric(label="🚀 **Total Não Treineiro**", value=formatted_total_treineiro_nao)

st.markdown("---")

# Exibir gráficos conforme a opção escolhida no menu
if menu_option == "💰 Faixa de Renda":
    st.markdown("### 🔥 Top 5 Faixa de Renda")
    st.bar_chart(dfTop5FaixaDeRenda, x='FaixaDeRenda', y='QtdeAlunos', use_container_width=True)

elif menu_option == "🌎 Estados":
    st.markdown("### 🌎 Top 5 Estados com Mais Alunos")
    st.bar_chart(dfTop5QtdeAlunosPorUF, x="UF", y="QtdeAlunos", use_container_width=True)

elif menu_option == "🏫 Tipo de Escola":
    st.markdown("### 🏫 Tipo de Escola")

    # Criar gráfico de pizza
    sizes = dfTipoEscola['QTDALUNOS']
    labels = dfTipoEscola['TIPO DA ESCOLA']

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=['#2E86C1', '#28B463', '#F39C12', '#8E44AD'],
        textprops={'fontsize': 12, 'weight': 'bold'}
    )
    ax.set_title("📊 Distribuição por Tipo de Escola", fontsize=16, fontweight="bold")
    st.pyplot(fig)

# Mensagem final
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: gray;'>📌 Dados do ENEM 2023 processados e analisados com Python e Streamlit.</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'> Thaan Costa - DATA ANALYTICS / ENGINEER</h5>", unsafe_allow_html=True)

# Fechar o engine
engine.dispose()
