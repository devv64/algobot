import talib

def get_points(prices):
    points = 0
    macd, macdsignal, macdhist = talib.MACD(prices)
    rsi = talib.RSI(prices)
    mom = talib.MOM(prices)
    fastk, fastd = talib.STOCHRSI(prices)
    upper, middle, lower = talib.BBANDS(prices)


    if macd[-1] > 0:
        points += 1

    elif macd[-1] < 0:
        points -= 1

    if rsi[-1] < 30:
        points += 1

    elif rsi[-1] > 70:
        points -= 1

    if mom[-1] > 0:
        points += 1

    elif mom[-1] < 0:
        points -= 1

    if fastk[-1] < 20:
        points += 1

    elif fastk[-1] > 80:
        points -= 1

    if prices[-1] < lower[-1]:
        points += 1

    elif prices[-1] > upper[-1]:
        points -= 1

    return points
