from fastapi import FastAPI
import pandas as pd
import joblib
from prophet.serialize import model_from_json
from prophet.plot import plot_plotly
from pydantic import BaseModel

# Inicializar app
app = FastAPI(title="Crypto Forecast API")

# Carregar modelo Prophet treinado
with open("model/bitcoin_forecast_model.pkl", "rb") as f:
    model = joblib.load(f)

# Modelo de entrada
class ForecastRequest(BaseModel):
    days: int = 30

# Rota principal
@app.get("/")
def home():
    return {"message": "🚀 API para previsão de preços de Bitcoin com Prophet"}

# Endpoint de previsão
@app.get("/predict")
def predict(days: int = 30):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    forecast = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(days)
    return forecast.to_dict(orient="records")
