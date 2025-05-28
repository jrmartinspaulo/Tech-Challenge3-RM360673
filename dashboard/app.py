import streamlit as st
import pandas as pd
import joblib
from prophet.plot import plot_plotly

# Carregar modelo e dados
model = joblib.load("model/bitcoin_forecast_model.pkl")
df = pd.read_csv("data/bitcoin_prices.csv")
df.rename(columns={"date": "ds", "price": "y"}, inplace=True)

# Prever os próximos 30 dias
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Título
st.title("📈 Previsão de Preço do Bitcoin (USD)")

# Mostrar gráfico interativo
fig = plot_plotly(model, forecast)
st.plotly_chart(fig)

# Mostrar dados
st.subheader("Previsões futuras")
st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30))
