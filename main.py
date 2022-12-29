from asyncio import proactor_events
import time
# from td.client import TDClient
import numpy as np
from scrape import get_price
from datetime import datetime
from points import get_points
import yfinance as yf
from supres import get_supports, get_resistance
import talib
# import psycopg2
# from zipline.api import order_target, record, symbol

# conn = psycopg2.connect("dbname=algobot user=postgres password=postgres")
# cur = conn.cursor()

# TDSession = TDClient(
#     client_id='',
#     redirect_uri='http://localhost:5500/',
#     credentials_path='./td_state.json'
# )

# TDSession.login()

prices = np.empty(0)
buy = False
buy_price = 0
minute = 0
f = open("log.txt", "a")
profit = 0

# atr = talib.ATR(prices['High'], prices['Low'], prices['Close'], timeperiod=5)

def printProfit():
    print("total P/L of the day: ", profit)
    # f.write("total P/L of the day: " + prices + '\n')

while True:
    curr_time = datetime.now()

    if curr_time.hour >= 9 and curr_time.hour < 16:
        prices = np.append(prices, float(get_price('SPY')))

        if len(prices) > 34:
            prices = np.delete(prices, 0)
            points = get_points(prices)
            # print(points)

            if points > 2 and not buy:
                buy = True
                buy_price = prices[-1]
                # print('atr: ', atr, '\n')
                print(curr_time, 'buy price:', prices[-1])
                # cur.execute("INSERT INTO pl (price, buy) VALUES ({}, {})".format(prices[-1], True))
                f.write(str(curr_time) + ' buy price: ' + str(prices[-1]) + '\n')

            elif points < -2 and buy:
                # print('atr: ', atr, '\n')
                print(curr_time, 'sell price:', prices[-1], 'profit:', prices[-1] - buy_price)
                # cur.execute("INSERT INTO pl (price, buy) VALUES ({}, {})".format(prices[-1], False))
                f.write(str(curr_time) + ' sell price: ' + str(prices[-1]) + ' profit: ' + str(prices[-1] - buy_price) + '\n')
                profit += prices[-1] - buy_price
                buy = False

        if minute != curr_time.minute:
            candles = yf.download(tickers="SPY", period="1d", interval="1m")
            get_supports(candles)
            get_resistance(candles)
            minute = curr_time.minute

    elif curr_time.hour == 16 and curr_time.minute == 0 and curr_time.second == 1:
        printProfit()

    time.sleep(1)


