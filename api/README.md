# 📈 Tech Challenge — Previsão de Preço de Criptomoedas (Bitcoin)

Este projeto foi desenvolvido como parte do **Tech Challenge da FIAP**. Ele reúne os conhecimentos adquiridos em coleta de dados, machine learning, APIs e visualização interativa de dados. Nosso objetivo é **prever o preço do Bitcoin** com base em dados históricos usando um modelo de séries temporais.

---

## 🎯 Objetivo

- Criar um pipeline completo de ciência de dados:
  - Coleta de dados em tempo real com API pública (CoinGecko)
  - Armazenamento local dos dados
  - Treinamento de modelo de machine learning (Prophet)
  - Criação de uma API com FastAPI para servir o modelo
  - Construção de um dashboard com Streamlit para visualização das previsões
  - Documentação e apresentação final em vídeo

---

## 🧠 Tecnologias Utilizadas

- `Python`
- `pandas`, `requests`, `prophet`
- `FastAPI` + `Uvicorn` (API)
- `Streamlit` (dashboard)
- `CoinGecko API` (fonte de dados)
- `GitHub` (versão final com código/documentação)

---

## 📦 Estrutura do Projeto

Tech-Challenge3-RM360673/
├── api/
│ └── main.py # API com endpoint de previsão
├── data/
│ └── coingecko_collector.py # Coletor de dados históricos do Bitcoin
├── db/
│ └── db_utils.py
├── model/
│ └── train_model.py # Treinamento do modelo Prophet
├── dashboard/
│ └── app.py # Visualização interativa com Streamlit
├── README.md # Documentação do projeto
├── requirements.txt # Bibliotecas utilizadas
└── venv/ # Ambiente virtual