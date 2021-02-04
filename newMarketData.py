#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import re
import yfinance as yf

def getTicker(s):
    regex = r"ipocalendar\">(\w+)"
    match = re.findall(regex, s)
    newmatch = ""
    for i in match[0]:
        if(i == " "):
            break
        else:
            newmatch += i
        
    print("Ticker: " + newmatch)
    return newmatch

def getCompany(s):
    regex = r"ipocalendar\">(.*)\s?<"
    match = re.findall(regex, s)
    print("Company Name: " + match[0])

def getData(ticker):
    try:
        data = yf.Ticker(ticker)
        print("Market Open: " + str(data.info['regularMarketOpen']))
        print("Market Close: " + str(data.info['previousClose']))
        print("50 Day Average: " + str(data.info['fiftyDayAverage']))
    except:
        print("An error occured")

url = "https://www.marketwatch.com/tools/ipo-calendar"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find('table', {'class': 'table table--primary ranking table--overflow tool-table'})

regex = r"<td.*?>(.*)<\/td>"
ans = re.findall(regex, str(table))

titles = ["Company Name", "Ticker", "Market", "Original Stock Price", "Shares", "IPO Date"]

cnt = 0
for x in ans:
    if(cnt == 6):
        print()
        cnt = 0
    newStr = titles[cnt] + ": " + x
    if(newStr[0] == 'T'):
        print(newStr)
        tick = getTicker(newStr)
        getData(tick)
    elif(newStr[0] == 'C'):
        print(newStr)
        getCompany(newStr)
    else:
        print(newStr)
    cnt+=1

input('Press ENTER to exit')





