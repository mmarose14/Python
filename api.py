# API operations
# Utilizes IEX API: https://iexcloud.io/docs/api/

import config
import requests
import json
from datetime import datetime

#Switch environment
#ENV = "sandbox"
ENV = "cloud"

def isSandbox(): return (ENV == "sandbox")

#Retrieve data for list of symbols
def getDividendDataForListOfSymbols(ListOfSymbols):
    data = []
    for symbol in ListOfSymbols:
        print(f"Processing {symbol}...")
        #Endpoint for next dividend date
        url = f"https://{ENV}.iexapis.com/stable/data-points/{symbol}/NEXTDIVIDENDDATE?token={config.API_TOKEN}"
        ex_div_date = getTickerData(url)

        #Endpoint for dividend yield
        url = f"https://{ENV}.iexapis.com/stable/data-points/{symbol}/DIVIDENDYIELD?token={config.API_TOKEN}"
        div_yield = getTickerData(url)

        div_yield = round(100 * div_yield, 2)

        symbol_data = {}
        symbol_data['symbol'] = symbol
        symbol_data['ex_div_date'] = ex_div_date
        symbol_data['div_yield'] = div_yield
    
        data.append(symbol_data)
    
    #Return sorted by date
    return sorted(data, key=lambda r: r['ex_div_date'])

#Retrieve data from url endpoint
def getTickerData(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
