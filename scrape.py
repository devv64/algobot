from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_price(ticker):
    url = 'https://finance.yahoo.com/quote/{}?p={}'.format(ticker, ticker)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get('value')
    return price

