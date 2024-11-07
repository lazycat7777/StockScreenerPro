import talib


def calculate_indicators(data):
    data['range'] = data['high'] - data['low']
    adr_percent = 100 * (data['range'] / data['low']).rolling(window=20).mean().iloc[-1]

    SMA_10 = talib.SMA(data['close'], timeperiod=10)
    SMA_20 = talib.SMA(data['close'], timeperiod=20)
    SMA_50 = talib.SMA(data['close'], timeperiod=50)
    SMA_100 = talib.SMA(data['close'], timeperiod=100)
    SMA_150 = talib.SMA(data['close'], timeperiod=150)
    SMA_200 = talib.SMA(data['close'], timeperiod=200)
    
    high_10 = data['high'].rolling(window=10).max().iloc[-1]
    high_20 = data['high'].rolling(window=20).max().iloc[-1]
    high_50 = data['high'].rolling(window=50).max().iloc[-1]
    high_100 = data['high'].rolling(window=100).max().iloc[-1]
    high_150 = data['high'].rolling(window=150).max().iloc[-1]
    high_200 = data['high'].rolling(window=200).max().iloc[-1]
    high_1y = data['high'].rolling(window=252).max().iloc[-1]

    low_10 = data['low'].rolling(window=10).min().iloc[-1]
    low_20 = data['low'].rolling(window=20).min().iloc[-1]
    low_50 = data['low'].rolling(window=50).min().iloc[-1]
    low_100 = data['low'].rolling(window=100).min().iloc[-1]
    low_150 = data['low'].rolling(window=150).min().iloc[-1]
    low_200 = data['low'].rolling(window=200).min().iloc[-1]
    low_1y = data['low'].rolling(window=252).min().iloc[-1]

    return {
        'ADR_percent': adr_percent,
        'SMA_10': SMA_10.iloc[-1],
        'SMA_20': SMA_20.iloc[-1],
        'SMA_50': SMA_50.iloc[-1],
        'SMA_100': SMA_100.iloc[-1],
        'SMA_150': SMA_150.iloc[-1],
        'SMA_200': SMA_200.iloc[-1],
        'High_10': high_10,
        'High_20': high_20,
        'High_50': high_50,
        'High_100': high_100,
        'High_150': high_150,
        'High_200': high_200,
        'High_1Y': high_1y,
        'Low_10': low_10,
        'Low_20': low_20,
        'Low_50': low_50,
        'Low_100': low_100,
        'Low_150': low_150,
        'Low_200': low_200,
        'Low_1Y': low_1y
    }