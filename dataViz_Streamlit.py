import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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
    st.markdown("### 🔥 Top 5 Distribuição por Faixa de Renda")

    # Criar o gráfico de barras com melhorias
    fig, ax = plt.subplots(figsize=(8, 5))

    # Escolher uma paleta de cores mais sofisticada
    colors = sns.color_palette("muted", len(dfTop5FaixaDeRenda))

    bars = ax.bar(
        dfTop5FaixaDeRenda['FaixaDeRenda'],
        dfTop5FaixaDeRenda['QtdeAlunos'],
        color=colors,
        edgecolor='none',  # Removendo bordas das barras
        linewidth=1.2
    )

    # Melhorando a formatação dos eixos
    #ax.set_xlabel("Faixa de Renda", fontsize=12, fontweight="bold")
    #ax.set_ylabel("Quantidade de Alunos", fontsize=12, fontweight="bold")
    #ax.set_title("📊 Distribuição por Faixa de Renda", fontsize=14, fontweight="bold", pad=15)

    # Melhorando a rotação dos rótulos para não ficarem cortados
    ax.set_xticklabels(
        dfTop5FaixaDeRenda['FaixaDeRenda'], 
        rotation=30, 
        ha="right", 
        fontsize=10, 
        fontweight="bold",
        wrap=True
    )

    # Adicionando os valores acima das barras para melhor visualização
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 20000, f"{int(yval):,}".replace(",", "."), 
                ha='center', va='bottom', fontsize=10, fontweight="bold", color='white')

    # Removendo a borda do gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Ajustar layout para evitar cortes
    plt.tight_layout()

    # Exibir no Streamlit
    st.pyplot(fig)


elif menu_option == "🌎 Estados":
    st.markdown("### 🌎 Top 5 Estados com Mais Inscritos")
    
    #st.bar_chart(dfTop5QtdeAlunosPorUF, x="UF", y="QtdeAlunos", use_container_width=True)

    # Criar o gráfico de barras com melhorias
    fig, ax = plt.subplots(figsize=(8, 5))

    # Escolher uma paleta de cores mais sofisticada
    colors = sns.color_palette("muted", len(dfTop5QtdeAlunosPorUF))

    bars = ax.bar(
        dfTop5QtdeAlunosPorUF['UF'],
        dfTop5QtdeAlunosPorUF['QtdeAlunos'],
        color=colors,
        edgecolor='none',  # Removendo bordas das barras
        linewidth=1.2
    )

     # Melhorando a rotação dos rótulos para não ficarem cortados
    ax.set_xticklabels(
        dfTop5QtdeAlunosPorUF['UF'], 
        rotation=30, 
        ha="right", 
        fontsize=10, 
        fontweight="bold",
        wrap=True
    )

    # Adicionando os valores acima das barras para melhor visualização
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 20000, f"{int(yval):,}".replace(",", "."), 
                ha='center', va='bottom', fontsize=10, fontweight="bold", color='white')

    # Removendo a borda do gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Ajustar layout para evitar cortes
    plt.tight_layout()

    # Exibir no Streamlit
    st.pyplot(fig)



elif menu_option == "🏫 Tipo de Escola":
    st.markdown("### 🏫 Distribuição por Tipo de Escola")

    # Criar gráfico de pizza com melhorias
    sizes = dfTipoEscola['QTDALUNOS']
    labels = dfTipoEscola['TIPO DA ESCOLA']
    colors = ['#4C78A8', '#F58518', '#54A24B']  # Azul, Laranja, Verde

    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        textprops={'fontsize': 12, 'weight': 'bold'}
    )

    # Melhorar legibilidade das labels
    for text in texts:
        text.set_fontsize(14)
        text.set_fontweight('bold')

    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
        autotext.set_color('white')

    # Melhorar título e layout
    #ax.set_title("📊 Distribuição por Tipo de Escola", fontsize=16, fontweight="bold", pad=20)
    
    # Ajustar layout para evitar cortes
    plt.tight_layout()

    st.pyplot(fig)

# Mensagem final
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: gray;'>📌 Dados do ENEM 2023 processados e analisados com Python e Streamlit.</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'> Thaan Costa - DATA ANALYTICS / ENGINEER</h5>", unsafe_allow_html=True)

# Fechar o engine
engine.dispose()
