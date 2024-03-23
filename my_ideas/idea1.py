import json
import requests


def get_all_binance_price():
    api_url = 'https://api.binance.com/api/v1/ticker/price?symbols=["BTCUSDT","ETHUSDT","BNBUSDT"]'
    response = json.loads(requests.get(api_url).content)
    return response


prices_json = get_all_binance_price()

for item in prices_json:
    print(item["symbol"] + " " + str(round(float(item["price"]), 2)) + " USDT")
