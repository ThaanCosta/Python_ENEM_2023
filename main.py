from tqdm import tqdm
from sqlalchemy import create_engine
import pandas as pd
from app.db_config import database_config

# Exemplo de como carregar ou criar o DataFrame (ajuste conforme necessário)
dadosQstSocioEconTratamento = pd.DataFrame({
    'NU_INSCRICAO': ['210059085136'] * 1000,
    'Q001': ['A'] * 1000,
    'Q002': ['F'] * 1000,
    'Q003': ['E'] * 1000,
    # Adicione outras colunas conforme necessário
})

# Transformar dados com melt (ou conforme necessário)
dadosUnpivot = dadosQstSocioEconTratamento.melt(
    id_vars=['NU_INSCRICAO'],
    var_name='Questoes',
    value_name='Resposta'
)

# Criação da string de conexão
connection_string = (
    f"mssql+pyodbc://{database_config['username']}:{database_config['password']}"
    f"@{database_config['host']}/{database_config['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Crie o engine do SQLAlchemy
engine = create_engine(connection_string)

chunk_size = 100000  # Defina o tamanho do chunk conforme necessário
total_chunks = (len(dadosUnpivot) // chunk_size) + 1  # Calcula o número total de chunks

try:
    with tqdm(total=total_chunks, desc="Inserindo dados no banco") as pbar:
        for start in range(0, len(dadosUnpivot), chunk_size):
            end = min(start + chunk_size, len(dadosUnpivot))
            chunk = dadosUnpivot.iloc[start:end]
            chunk.to_sql('RespostaQstSocEconomico', con=engine, if_exists='append', index=False)
            pbar.update(1)  # Atualiza a barra de progresso
    print("Dados inseridos com sucesso!")
except Exception as e:
    print("Erro ao inserir os dados:", e)
