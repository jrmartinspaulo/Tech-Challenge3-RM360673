import pandas as pd
from prophet import Prophet
import joblib

# Carregar os dados
df = pd.read_csv("data/bitcoin_prices.csv")

# Renomear colunas para o formato do Prophet
df.rename(columns={"date": "ds", "price": "y"}, inplace=True)

# Criar e treinar modelo
model = Prophet(daily_seasonality=True)
model.fit(df)

# Salvar modelo treinado
joblib.dump(model, "model/bitcoin_forecast_model.pkl")
print("✅ Modelo treinado e salvo em 'model/bitcoin_forecast_model.pkl'")