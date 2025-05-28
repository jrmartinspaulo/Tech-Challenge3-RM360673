import requests
import pandas as pd
from datetime import datetime

# Função para converter timestamps
def convert_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)

# Buscar dados históricos de preço do Bitcoin
def fetch_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "90",  # últimos 90 dias
        "interval": "daily"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]

        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["date"] = df["timestamp"].apply(convert_to_datetime)
        df = df[["date", "price"]]
        df.to_csv("data/bitcoin_prices.csv", index=False)
        print("✅ Dados salvos em 'data/bitcoin_prices.csv'")
    else:
        print(f"Erro na requisição: {response.status_code}")

if __name__ == "__main__":
    fetch_bitcoin_data()
