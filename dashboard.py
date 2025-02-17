# %%
import pandas as pd
import pyodbc
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import snowflake.connector

from sqlalchemy import create_engine
from config.db_config import database_config
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Construa a string de conexão corretamente formatada
connection_string = (
    f"mssql+pyodbc://{database_config['username']}:{database_config['password']}"
    f"@{database_config['host']}/{database_config['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Crie o engine do SQLAlchemy
engine = create_engine(connection_string)


# %%
queryTop5QtdeAlunosPorUF = """ 
    SELECT COUNT(P.NU_INSCRICAO) AS QtdeAlunos,
           LP.SG_UF_PROVA as UF
    FROM DadosParticipantes P
    INNER JOIN DadosFatoEnem2023 F ON F.NU_INSCRICAO = P.NU_INSCRICAO
    INNER JOIN DadosLocalAplProva LP ON LP.CO_MUNICIPIO_PROVA = F.CO_MUNICIPIO_PROVA
    GROUP BY LP.SG_UF_PROVA
    ORDER BY LP.SG_UF_PROVA
    OFFSET 0 ROWS
    FETCH NEXT 5 ROWS ONLY
"""

# Carregar os dados no DataFrame
dfTop5QtdeAlunosPorUF = pd.read_sql(queryTop5QtdeAlunosPorUF, engine)

# Querie que retorna o Top 5 por Faixa de Renda
queryTop5FaixaDeRenda = """
    SELECT COUNT(P.NU_INSCRICAO) AS QtdeAlunos,
           Q.DESC_RESPOSTA AS FaixaDeRenda
    FROM DadosParticipantes P
    INNER JOIN RespostaQstSocEconomico Resp ON Resp.NU_INSCRICAO = P.NU_INSCRICAO
    INNER JOIN QstSocEconomico Q ON Resp.Questoes = Q.ID_QUESTIONARIO AND Resp.Resposta = Q.NR_REPOSTA
    WHERE Q.ID_QUESTIONARIO = 'Q006'
    GROUP BY Q.DESC_RESPOSTA
    ORDER BY QtdeAlunos DESC
    OFFSET 0 ROWS
    FETCH NEXT 5 ROWS ONLY
"""
# Carregar os dados no DataFrame
dfTop5FaixaDeRenda = pd.read_sql(queryTop5FaixaDeRenda, engine)


querieTotalInscritos = """
    select COUNT(1) as TotalInscritos
    from DadosFatoEnem2023
"""
dfTotalInscritos = pd.read_sql(querieTotalInscritos, engine)

# Extraia e formate o valor do DataFrame
total_inscritos = dfTotalInscritos['TotalInscritos'][0]
formatted_total_inscritos = f"{total_inscritos:,.0f}"  # Formata o número com separadores de milhar
formatted_total_inscritos = formatted_total_inscritos.replace(',', '.')  # Substitui vírgulas por pontos


querieTotalTreineiros_SIM = """
    select Count(1) as 'Treineiro'
    from DadosParticipantes
    where IN_TREINEIRO =  'Sim'
"""
dfTotalTreineirosSim = pd.read_sql(querieTotalTreineiros_SIM, engine)
total_treineiro_sim = dfTotalTreineirosSim['Treineiro'][0]
formatted_total_treineiro_sim = f"{total_treineiro_sim:,.0f}"
formatted_total_treineiro_sim = formatted_total_treineiro_sim.replace(',','.')

querieTotalTreineiros_NAO = """
    select Count(1) as 'Não Treineiro'
    from DadosParticipantes
    where IN_TREINEIRO =  'Não'
"""
dfTotalTreineirosNao = pd.read_sql(querieTotalTreineiros_NAO, engine)
total_treineiro_nao = dfTotalTreineirosNao['Treineiro'][0]
formatted_total_treineiro_nao = f"{total_treineiro_nao:,.0f}"
formatted_total_treineiro_nao = formatted_total_treineiro_nao.replace(',','.')

# Fechar o engine
engine.dispose()

# %%

st.metric(label="Total Inscritos", value=formatted_total_inscritos)

# %%
#Criando um menu lateral para melhorar a navegação
with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Overview","Analise Notas","Socio Economico","Linkedin"],
    icons = ["house","activity","gear","envelope"],
    menu_icon = "cast",
    default_index = 0,
)
    


# %%
if selected == "Overview":
    st.header('Overview Informações Enem - 2023')
    # Criar duas colunas no layout do Streamlit
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 5 Estados por Número de Alunos")
        st.dataframe(dfTop5QtdeAlunosPorUF)

        st.subheader("Distribuição por Estado")
        st.bar_chart(dfTop5QtdeAlunosPorUF.set_index('UF'))

    with col2:
        st.subheader("Top 5 Faixas de Renda")
        st.dataframe(dfTop5FaixaDeRenda)

        st.subheader("Distribuição por Faixa de Renda")
        st.bar_chart(dfTop5FaixaDeRenda.set_index('FaixaDeRenda'))

    