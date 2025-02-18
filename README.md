# 📊 Projeto ENEM 2023 - Data Lakehouse

Este repositório contém a implementação de um **Data Lakehouse** para análise dos dados do **ENEM 2023**, utilizando **Python, Pandas, Streamlit e SQL Server**. O projeto foi desenvolvido para organizar, processar e visualizar os microdados do ENEM, permitindo a criação de insights interativos e painéis analíticos.

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Pandas** para manipulação de dados
- **Streamlit** para visualização interativa
- **Matplotlib & Seaborn** para geração de gráficos
- **SQL Server** para armazenamento estruturado
- **SQLAlchemy** para conexão com banco de dados
- **Docker** para gerenciamento do ambiente
- **Git/GitHub** para versionamento

## 📁 Estrutura do Projeto

```
Python_ENEM_2023/
│── app/               # Aplicação Streamlit para visualização dos dados
│── src/               # Código-fonte para ETL e manipulação de dados
│   ├── cargasTabelasDim_Fato/   # Scripts de carga das tabelas dimensionais
│── scripts/           # Scripts SQL para criação e consultas no banco
│── docs/              # Documentação do projeto
│── queries/           # Queries SQL utilizadas na aplicação
│── dataViz_Streamlit.py  # Script principal da aplicação Streamlit
│── README.md          # Documentação do projeto
│── requirements.txt   # Dependências do projeto
│── Dockerfile         # Arquivo para containerização
```

## ⚙️ Como Executar o Projeto

### 1️⃣ **Clone o repositório**
```sh
git clone https://github.com/ThaanCosta/Python_ENEM_2023.git
cd Python_ENEM_2023
```

### 2️⃣ **Crie um ambiente virtual e instale as dependências**
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3️⃣ **Executar a aplicação Streamlit**
```sh
streamlit run dataViz_Streamlit.py
```

### 4️⃣ **Executar os scripts de ETL**
```sh
python src/camadasRaw.py
python src/cargasTabelasDim_Fato/main.py
```

## 📊 Dashboards e Visualização
Os dados processados são visualizados em painéis interativos gerados com **Streamlit**.

### 🔥 **Exemplo de gráficos gerados**
#### Distribuição por Faixa de Renda
![Distribuição Faixa de Renda](docs/faixa_renda.png)

#### Top 5 Estados com Mais Inscritos
![Distribuição por Estado](docs/top5_estados.png)

#### Tipo de Escola
![Distribuição por Tipo de Escola](docs/tipo_escola.png)


## 🛠 Funcionalidades da Aplicação
✅ **KPI’s** – Exibição de métricas-chave (Total de Inscritos, Treineiros e Não Treineiros)  
✅ **Visualizações** – Gráficos interativos sobre faixa de renda, estados e tipos de escola  
✅ **Consultas SQL** – Extração de dados diretamente do banco SQL Server  
✅ **Painéis Interativos** – Criados com **Streamlit** para fácil exploração dos dados  

## 🤝 Contribuindo
Fique à vontade para abrir **Issues** e **Pull Requests** com melhorias ou sugestões para o projeto.

## 📩 Contato
**Desenvolvedor:** Thaan Costa  
📧 Email: [thaancosta@gmail.com](mailto:thaancosta@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/thaancosta](https://www.linkedin.com/in/thaancosta)  

---

Este projeto é mantido como um estudo e exemplo de boas práticas na construção de um **Data Lakehouse** para análise de dados educacionais. 📚🚀

