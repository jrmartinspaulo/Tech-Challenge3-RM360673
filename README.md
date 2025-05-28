1. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt

2. Coletar dados do Bitcoin
bash
Copiar
Editar
python data/coingecko_collector.py

3. Treinar o modelo Prophet
bash
Copiar
Editar
python model/train_model.py

4. Iniciar a API
bash
Copiar
Editar
uvicorn api.main:app --reload
Acesse: http://127.0.0.1:8000/docs para testar a API.

5. Executar o dashboard
bash
Copiar
Editar
streamlit run dashboard/app.py

🧪 Exemplos de uso da API
Método	Rota	Descrição
GET	/	Mensagem inicial da API
GET	/predict?days=30	Retorna a previsão de preços para os próximos 30 dias
GET	/docs	Interface Swagger para testar a API
