
import pandas as pd
import datetime
import yfinance as yf
from yahoo_fin import stock_info as si
import re

# def getData(ticker):

#     while True:
#         data = yf.Ticker(ticker)
#         print("Current Price: " + str(data.info['regularMarketPrice']))
#         print("Market Open: " + str(data.info['regularMarketOpen']))
#         print("Market Close: " + str(data.info['previousClose']))
#         print("50 Day Average: " + str(data.info['fiftyDayAverage']))
#         print("200 Day Average: " + str(data.info['twoHundredDayAverage']))
#         print(data.info)


#getData('GME')
print("Enter stock ticker: ")
ticker = input()
print("Current Price: " + str(si.get_live_price(ticker)))
# get most active stocks on the day
print("Most Active:\n " + str(si.get_day_most_active()))
# get biggest gainers
print("Biggest Gainers:\n " + str(si.get_day_gainers()))
# get worst performers
print("Worst performers:\n " + str(si.get_day_losers()))




 