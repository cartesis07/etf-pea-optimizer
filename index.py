import pandas_datareader.data as web
import datetime
import pandas as pd 

import urllib3
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,9,12)



def get_stock(ticker):
    data = web.DataReader(f"{ticker}","yahoo",start,end)
    data[f'{ticker}'] = data["Close"]
    data = data[[f'{ticker}']] 
    print(data.head())
    return data

pfizer = get_stock("PFE")
jnj = get_stock("JNJ")

http = urllib3.PoolManager()
r = http.request('GET', 'https://api.twelvedata.com/time_series?symbol=LYMTA&interval=1day&apikey=df509dfdfc9f4e54ac460d48c447c30e')

print(json.loads(r.data.decode('utf-8')))

# https://swapi.dev/api/starships/9/ example url

# def get_etf(ticker):
