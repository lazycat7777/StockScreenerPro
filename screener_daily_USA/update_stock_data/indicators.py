import talib


def calculate_indicators(data):
    # ADR%
    data['range'] = data['high'] - data['low']
    adr_percent = 100 * (data['range'] / data['low']).rolling(window=20).mean().iloc[-1] 

    SMA_10 = talib.SMA(data['close'], timeperiod=10)
    SMA_20 = talib.SMA(data['close'], timeperiod=20)
    SMA_50 = talib.SMA(data['close'], timeperiod=50)
    SMA_100 = talib.SMA(data['close'], timeperiod=100)
    SMA_150 = talib.SMA(data['close'], timeperiod=150)
    SMA_200 = talib.SMA(data['close'], timeperiod=200)
    ema = talib.EMA(data['close'], timeperiod=10)
    rsi = talib.RSI(data['close'], timeperiod=10)

    return {
        'Price': data['close'].iloc[-1],
        'ADR_percent': adr_percent,
        'SMA_10': SMA_10.iloc[-1],
        'SMA_20': SMA_20.iloc[-1],
        'SMA_50': SMA_50.iloc[-1],
        'SMA_100': SMA_100.iloc[-1],
        'SMA_150': SMA_150.iloc[-1],
        'SMA_200': SMA_200.iloc[-1],
        'EMA': ema.iloc[-1],
        'RSI': rsi.iloc[-1]
    }