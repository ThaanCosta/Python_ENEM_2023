# 📊 Projeto ENEM 2023 - Data Lakehouse

Este repositório contém a implementação de um **Data Lakehouse** para análise dos dados do **ENEM 2023**, utilizando **Python, Pandas e SQL**. O projeto foi desenvolvido para organizar e processar os microdados do ENEM, permitindo a criação de insights e dashboards interativos.

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Pandas** para manipulação de dados
- **Streamlit** para visualização interativa
- **SQL Server** para armazenamento estruturado
- **Docker** para gerenciamento do ambiente
- **Git/GitHub** para versionamento

## 📁 Estrutura do Projeto

```
Python_ENEM_2023/
│── app/               # Aplicação Streamlit para visualização dos dados
│── src/               # Código-fonte para ETL e manipulação de dados
│── docs/              # Documentação do projeto
│── scripts/           # Scripts auxiliares
│── data/              # Arquivos de entrada (microdados do ENEM)
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
streamlit run app/main.py
```

### 4️⃣ **Executar os scripts de ETL**
```sh
python src/process_data.py
```

## 📊 Dashboards e Visualização
Os dados tratados podem ser visualizados em dashboards criados com **Streamlit**. Para acessar, basta rodar o comando acima e abrir o navegador no endereço fornecido pelo Streamlit.

## 🤝 Contribuindo
Fique à vontade para abrir **Issues** e **Pull Requests** com melhorias ou sugestões para o projeto.

## 📩 Contato
**Data Engineer | Analytics:** Thaan Costa  
📧 Email: [seuemail@email.com](mailto:thaancosta@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/seulinkedin](https://www.linkedin.com/in/thaancosta/) 

---

Este projeto é mantido como um estudo e exemplo de boas práticas na construção de um **Data Lakehouse** para análise de dados educacionais. 📚🚀

