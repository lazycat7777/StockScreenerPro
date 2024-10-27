from .symbols_and_exchanges_main import result_parser_of_symbols
from .models import StockData
from django.db import transaction
from tvDatafeed import TvDatafeed, Interval
import talib
import pandas as pd

# Отключение предупреждений о цепочечном присваивании
pd.options.mode.chained_assignment = None

# # Список символов и бирж

# symbols_and_exchanges = result_parser_of_symbols

symbols_and_exchanges = [
    ('AAM', 'NYSE'),
    ('BKV', 'NASDAQ'),
    ('CBNA', 'NASDAQ'),
    ('BKNG', 'NASDAQ'),
    ('MELI', 'NASDAQ'),
    ('ORLY', 'NASDAQ'),
    ('REAX', 'NASDAQ'),
    ('AAPL', 'NASDAQ'),
    ('GOOGL', 'NASDAQ'),
    ('BVS', 'NASDAQ'),
    ('LOVE', 'NASDAQ'),
    ('TREE', 'NASDAQ'),
    ('SLQT', 'NYSE'),
    ('RVMD', 'NASDAQ'),
    ('SLNO', 'NASDAQ'),
    ('COMP', 'NYSE'),
    ('SGHT', 'NASDAQ'),
    # Добавь сюда другие символы и биржи
]

interval = Interval.in_daily

# Подключение к TradingView
tv = TvDatafeed()

# Словарь для хранения данных по каждому символу
loaded_data = {}
for symbol, exchange in symbols_and_exchanges:
    loaded_data[(symbol, exchange)] = pd.DataFrame(columns=['open', 'high', 'low', 'close', 'volume']) 

# Функция для получения новых данных
def get_new_data(symbol, exchange, interval):
    global loaded_data
    key = (symbol, exchange)

    try:
        data = tv.get_hist(symbol, exchange=exchange, interval=interval, n_bars=500)
        if data is not None and not data.empty:
            # Обновление существующего DataFrame (объединение с новыми данными)
            loaded_data[key] = pd.concat([loaded_data[key], data], ignore_index=True)
            # Обновление цены закрытия
            return loaded_data[key]
        else:
            return None
    except Exception as e:
        return None


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


def calculate_and_aggregate_results():

    results = []

    # Общая таблица
    final_table = pd.DataFrame(columns=[
        'Symbol', 
        'Exchange', 
        'Price', 
        'ADR_percent',
        'SMA_10', 
        'SMA_20', 
        'SMA_50',
        'SMA_100',
        'SMA_150',
        'SMA_200',
        'EMA', 
        'RSI'
        ])

    for symbol, exchange in symbols_and_exchanges:

        new_data = get_new_data(symbol, exchange, interval)

        if new_data is not None:
            indicators_dict = calculate_indicators(new_data)

            results.append({
                'Symbol': symbol,
                'Exchange': exchange,
                'Price': indicators_dict['Price'],
                'ADR_percent': indicators_dict['ADR_percent'],
                'SMA_10': indicators_dict['SMA_10'],
                'SMA_20': indicators_dict['SMA_20'],
                'SMA_50': indicators_dict['SMA_50'],
                'SMA_100': indicators_dict['SMA_100'],
                'SMA_150': indicators_dict['SMA_150'],
                'SMA_200': indicators_dict['SMA_200'],
                'EMA': indicators_dict['EMA'],
                'RSI': indicators_dict['RSI'] 
            })

    # После завершения цикла добавляем все результаты в таблицу
    if results:
        final_table.drop(final_table.index, inplace=True)
        final_table = pd.concat([final_table, pd.DataFrame(results)], ignore_index=True)
        results = []  # очищаем список для новых результатов

    # Очистка таблицы в базе данных перед сохранением новых данных
    StockData.objects.all().delete()

    # Сохраняем данные в одном транзакционном блоке
    with transaction.atomic():
        final_table_in_db = [
            StockData(
                symbol=vals['Symbol'], 
                exchange=vals['Exchange'], 
                price=round(float(str(vals['Price']).replace(',', '')), 2),
                ADR_percent=round(float(str(vals['ADR_percent']).replace(',', '')), 2),
                SMA_10=round(float(str(vals['SMA_10']).replace(',', '')), 2),
                SMA_20=round(float(str(vals['SMA_20']).replace(',', '')), 2),
                SMA_50=round(float(str(vals['SMA_50']).replace(',', '')), 2),
                SMA_100=round(float(str(vals['SMA_100']).replace(',', '')), 2),
                SMA_150=round(float(str(vals['SMA_150']).replace(',', '')), 2),
                SMA_200=round(float(str(vals['SMA_200']).replace(',', '')), 2),
                ema=round(float(str(vals['EMA']).replace(',', '')), 2),
                rsi=round(float(str(vals['RSI']).replace(',', '')), 2)
            ) for vals in final_table.to_dict(orient='records')
        ]
        
        # Сохраняем все данные в базе данных
        StockData.objects.bulk_create(final_table_in_db)

    return final_table


