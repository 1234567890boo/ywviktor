import requests
import json

PRICE_QUERY_STRING='http://www.google.com/finance/historical?q={}&startdate={}&enddate={}&output=csv'

def stockprice(stock):
    json_data=requests.get(PRICE_QUERY_STRING.format(stock)).text
    json_data=json_data.replace("//",'')
    stock_price = float(json.loads(json_data)[0]['l'])
    return stock_price


startdate="Jan 1,1990"
enddate="Jan 1,2020"
stockhistoryquery="http://www.google.com/finance/historical?q={}&startdate={}&enddate={}&output=csv"

stockprice(stockhistoryquery)