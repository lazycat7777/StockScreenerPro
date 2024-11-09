from .symbols_and_exchanges_main import symbols_and_exchanges

from tvDatafeed import TvDatafeed, Interval
import pandas as pd

interval = Interval.in_daily

# Подключение к TradingView
tv = TvDatafeed()

# Словарь для хранения данных по каждому символу
loaded_data = {
    (symbol, exchange): pd.DataFrame(columns=['open', 'high', 'low', 'close', 'volume']) 
    for symbol, exchange in symbols_and_exchanges
}

# Функция для получения новых данных
def get_new_data(symbol, exchange, interval):
    key = (symbol, exchange)

    try:
        data = tv.get_hist(symbol, exchange=exchange, interval=interval, n_bars=300)
        if data is not None and not data.empty:
            # Обновление существующего DataFrame (объединение с новыми данными)
            loaded_data[key] = pd.concat([loaded_data[key], data], ignore_index=True)
            # Обновление цены закрытия
            return loaded_data[key]
        else:
            return None
    except Exception as e:
        return None