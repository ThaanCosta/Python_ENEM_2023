# %%

import pandas as pd
import sqlalchemy as sa  # Corrigido
from sqlalchemy import create_engine  # Importação correta para criar o engine
import os
import sys
sys.path.append(r'c:\Projetos\Python\JornadaDeDados')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# %%
df = pd.read_csv("c:/Projetos/Python/JornadaDeDados/microdados_enem_2023/DADOS/MICRODADOS_ENEM_2023.csv", delimiter=";", encoding="latin-1")

# %%
tabela = 'enem2023_dadosbrutos'

tipo_dado_map = {
    'int64': 'BIGINT',
    'float64': 'FLOAT',
    'object': 'VARCHAR({})',
    'bool': 'BIT',
    'datetime64[ns]': 'DATETIME'
}

def calcular_max_varchar_colunas(df, coluna):
    
    #retornar o comprimento máximo da coluna
    if df[coluna].dtype == 'object':
        return df[coluna].apply(lambda x: len(str(x))).max()
    return None


def gerar_sql_create_table(df, tabela):
    colunas = []
    
    for coluna, tipo in df.dtypes.items():
        if str(tipo) in tipo_dado_map:
            tipo_sql = tipo_dado_map[str(tipo)]
            if 'VARCHAR' in tipo_sql:
                max_length = calcular_max_varchar_colunas(df, coluna)
                if max_length is None:
                    max_length = 255  # Valor padrão caso não seja possível calcular
                tipo_sql = tipo_sql.format(max_length)
            colunas.append(f"[{coluna}] {tipo_sql}")
        else:
            colunas.append(f"[{coluna}] VARCHAR(MAX)")  # Tipo padrão para casos não mapeados
    
    sql_create = f"CREATE TABLE {tabela} (\n" + ",\n".join(colunas) + "\n);"
    return sql_create

# Gerando o script SQL
script_sql_create = gerar_sql_create_table(df, tabela)

# Exibe o script SQL, basta apenas copiar o result e colar no SSMS que será criado a tabela
print(script_sql_create)

# %%
from tqdm import tqdm
from sqlalchemy import create_engine
from app.db_config import database_config


def insert_data(df, config, table_name):
    connection_string = (
        f"mssql+pyodbc://{config['username']}:{config['password']}"
        f"@{config['host']}/{config['database']}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    engine = create_engine(connection_string)
    chunk_size = 100000
    total_chunks = (len(df) // chunk_size) + 1

try:
    with tqdm(total=total_chunks, desc="Inserindo dados no banco") as pbar:
        for start in range(0, len(df), chunk_size):
            end = min(start + chunk_size, len(df))
            chunk = df.iloc[start:end]
            chunk.to_sql('enem2023_dadosbrutos', con=engine, if_exists='append', index=False)
            pbar.update(1)  # Atualiza a barra de progresso
    print("Dados inseridos com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)

# %%
