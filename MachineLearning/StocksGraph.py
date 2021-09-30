import requests
import json

PRICE_QUERY_STRING="http://finance.google.com/finance/info?client=ig&q=AMZM"
json_data=requests.get(PRICE_QUERY_STRING.format("AMZN")).text
json_data=json_data.replace("//",'')
stock_price = float(json.loads(json_data)[0]['l'])

print(stock_price)