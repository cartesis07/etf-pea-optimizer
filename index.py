import pandas_datareader.data as web
import datetime
import pandas as pd 

import urllib3
http = urllib3.PoolManager()
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

# read etf list csv

import pandas as pd

etf_list = pd.read_csv('etf_list.csv')

print(etf_list.to_string())

# get etf history with marketstack

def get_etf(ticker):
    request = http.request('GET', 'http://api.marketstack.com/v1/eod?access_key=87a17751375d57c0a6dcecbfd9181246&symbols=' + ticker)
    #print(json.loads(request.data.decode('utf-8')))
    return request

asia = get_etf("AEJ.XPAR")
 
# https://swapi.dev/api/starships/9/ example url

# def get_etf(ticker):
