from datetime import datetime
# import psycopg2
import yfinance as yf

# conn = psycopg2.connect("dbname=algobot user=postgres password=postgres")
# cur = conn.cursor()

candles = yf.download(tickers="SPY", period="1y", interval="1d")

supports = []
resistance = []
f = open("supres.txt", "a")


def get_supports(df):
    if df['Low'][-3] < df['Low'][-4] and df['Low'][-3] < df['Low'][-2] and df['Low'][-2] < df['Low'][-1] and df['Low'][-4] < df['Low'][-5]:
        supports.append(df['Low'][-3])
        # cur.execute("INSERT INTO supres (price) VALUES ({})".format(df['Low'][-3]))
        f.write(str(datetime.now()) + ' support: ' + str(df['Low'][-3]) + '\n')
    return supports


def get_resistance(df):
    if df['High'][-3] > df['High'][-4] and df['High'][-3] > df['High'][-2] and df['High'][-2] > df['High'][-1] and df['High'][-4] > df['High'][-5]:
        resistance.append(df['High'][-3])
        # cur.execute("INSERT INTO supres (price) VALUES ({})".format(df['High'][-3]))
        f.write(str(datetime.now()) + ' resistance: ' + str(df['High'][-3]) + '\n')
    return resistance
