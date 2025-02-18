# %%

import pandas as pd
import sqlalchemy as sa  # Corrigido
from sqlalchemy import create_engine  # Importação correta para criar o engine
import os
import sys
sys.path.append(r'c:\Projetos\Python\JornadaDeDados')

pd.set_option('display.max_columns', None)

# %%
df = pd.read_csv("microdados_enem_2023/DADOS/MICRODADOS_ENEM_2023.csv", delimiter=";", encoding="latin-1")

# %%
df.head()

# %%
df.columns.values

#%%
colunasFato = [
    'NU_INSCRICAO', 
    'NU_ANO', 
    'CO_MUNICIPIO_ESC', 
    'CO_MUNICIPIO_PROVA', 
    'NU_NOTA_CN', 
    'NU_NOTA_CH', 
    'NU_NOTA_LC', 
    'NU_NOTA_MT', 
    'NU_NOTA_COMP1', 
    'NU_NOTA_COMP2', 
    'NU_NOTA_COMP3', 
    'NU_NOTA_COMP4', 
    'NU_NOTA_COMP5', 
    'NU_NOTA_REDACAO']

# %%
dadoFato = df.filter(items=colunasFato)

# %%
dadoFato.dtypes

# %%
tabela = 'DadosFatoEnem2023'

tipo_dado_map = {
    'int64': 'BIGINT',
    'float64': 'FLOAT',
    'object': 'VARCHAR({})',
    'bool': 'BIT',
    'datetime64[ns]': 'DATETIME'
}

def calcular_max_varchar_colunas(dadoFato, coluna):
    
    #retornar o comprimento máximo da coluna
    if dadoFato[coluna].dtype == 'object':
        return dadoFato[coluna].apply(lambda x: len(str(x))).max()
    return None


def gerar_sql_create_table(dadoFato, tabela):
    colunas = []
    
    for coluna, tipo in dadoFato.dtypes.items():
        if str(tipo) in tipo_dado_map:
            tipo_sql = tipo_dado_map[str(tipo)]
            if 'VARCHAR' in tipo_sql:
                max_length = calcular_max_varchar_colunas(dadoFato, coluna)
                if max_length is None:
                    max_length = 255  # Valor padrão caso não seja possível calcular
                tipo_sql = tipo_sql.format(max_length)
            colunas.append(f"[{coluna}] {tipo_sql}")
        else:
            colunas.append(f"[{coluna}] VARCHAR(MAX)")  # Tipo padrão para casos não mapeados
    
    sql_create = f"CREATE TABLE {tabela} (\n" + ",\n".join(colunas) + "\n);"
    return sql_create

# Gerando o script SQL
script_sql_create = gerar_sql_create_table(dadoFato, tabela)

# Exibe o script SQL, basta apenas copiar o result e colar no SSMS que será criado a tabela
print(script_sql_create)

# %%

#Etapa que insere os dados no banco de dados

from sqlalchemy import create_engine
from app.db_config import database_config

# Construa a string de conexão corretamente formatada
connection_string = (
    f"mssql+pyodbc://{database_config['username']}:{database_config['password']}"
    f"@{database_config['host']}/{database_config['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Crie o engine do SQLAlchemy
engine = create_engine(connection_string)

chunk_size = 100000  # Defina o tamanho do chunk conforme necessário
total_chunks = (len(dadoFato) // chunk_size) + 1  # Calcula o número total de chunks

try:
    with tqdm(total=total_chunks, desc="Inserindo dados no banco") as pbar:
        for start in range(0, len(dadoFato), chunk_size):
            end = min(start + chunk_size, len(dadoFato))
            chunk = dadoFato.iloc[start:end]
            chunk.to_sql('DadosFatoEnem2023', con=engine, if_exists='append', index=False)
            pbar.update(1)  # Atualiza a barra de progresso
    print("Dados inseridos com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)

# %%
