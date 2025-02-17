# Queries a serem utilizadas no projeto ENEM
#Aqui ficara todo o código SQL que usaremos para mostrar os dados nos paineis.

# Query para contar o total de Inscritos
QUERY_TOTAL_INSCRITOS = """
    SELECT COUNT(1) AS TotalInscritos FROM DadosFatoEnem2023
"""

# Query para contar o total de treineiros SIM
QUERY_TOTAL_TREINEIROS_SIM = """
    SELECT COUNT(1) AS Sim_Treineiro FROM DadosParticipantes WHERE IN_TREINEIRO = 'Sim'
"""

# Query para contar o total de treineiros NÃO
QUERY_TOTAL_TREINEIROS_NAO = """
    SELECT COUNT(1) AS Nao_Treineiro FROM DadosParticipantes WHERE IN_TREINEIRO = 'Não'
"""

# Query para a faixa de renda
QUERY_TOP5_FAIXA_RENDA = """
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

# Query para os estados com mais alunos
QUERY_TOP5_QTDE_ALUNOS_UF = """ 
    SELECT COUNT(P.NU_INSCRICAO) AS QtdeAlunos,
           LP.SG_UF_PROVA as UF
    FROM DadosParticipantes P
    INNER JOIN DadosFatoEnem2023 F ON F.NU_INSCRICAO = P.NU_INSCRICAO
    INNER JOIN DadosLocalAplProva LP ON LP.CO_MUNICIPIO_PROVA = F.CO_MUNICIPIO_PROVA
    GROUP BY LP.SG_UF_PROVA
    ORDER BY QtdeAlunos DESC
    OFFSET 0 ROWS
    FETCH NEXT 5 ROWS ONLY
"""

# Query para tipo de escola
QUERY_TIPO_ESCOLA = """
    SELECT COUNT(NU_INSCRICAO) AS QTDALUNOS,
           TP_ESCOLA AS 'TIPO DA ESCOLA'
    FROM DadosParticipantes
    GROUP BY TP_ESCOLA
"""