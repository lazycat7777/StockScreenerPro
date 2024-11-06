from .connecting_to_tradingview import get_new_data
from .indicators import calculate_indicators
from .symbols_and_exchanges_main import symbols_and_exchanges
from .connecting_to_tradingview import interval

from ..models import StockData
from django.db import transaction
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


def calculate_and_aggregate_results():
    results = []

    # Общая таблица
    final_table = pd.DataFrame(columns=[
        'Symbol', 
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
                'Symbol': f"{exchange}:{symbol}",
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
        final_table = pd.concat([final_table, pd.DataFrame(results)], ignore_index=True)

    # Заменяем NaN на None перед сохранением в базу данных
    final_table = final_table.replace({np.nan: None})

    # Очистка таблицы в базе данных перед сохранением новых данных
    StockData.objects.all().delete()

    # Сохраняем данные в одном транзакционном блоке
    with transaction.atomic():
        final_table_in_db = []
        for vals in final_table.to_dict(orient='records'):
            final_table_in_db.append(
                StockData(
                    symbol=vals['Symbol'], 
                    ADR_percent=round(float(vals['ADR_percent']) if isinstance(vals['ADR_percent'], (float, int)) else (float(vals['ADR_percent'].replace(',', '')) if vals['ADR_percent'] not in [None, 'None'] else 0), 2) if vals['ADR_percent'] is not None else None,
                    SMA_10=round(float(vals['SMA_10']) if isinstance(vals['SMA_10'], (float, int)) else (float(vals['SMA_10'].replace(',', '')) if vals['SMA_10'] not in [None, 'None'] else 0), 2) if vals['SMA_10'] is not None else None,
                    SMA_20=round(float(vals['SMA_20']) if isinstance(vals['SMA_20'], (float, int)) else (float(vals['SMA_20'].replace(',', '')) if vals['SMA_20'] not in [None, 'None'] else 0), 2) if vals['SMA_20'] is not None else None,
                    SMA_50=round(float(vals['SMA_50']) if isinstance(vals['SMA_50'], (float, int)) else (float(vals['SMA_50'].replace(',', '')) if vals['SMA_50'] not in [None, 'None'] else 0), 2) if vals['SMA_50'] is not None else None,
                    SMA_100=round(float(vals['SMA_100']) if isinstance(vals['SMA_100'], (float, int)) else (float(vals['SMA_100'].replace(',', '')) if vals['SMA_100'] not in [None, 'None'] else 0), 2) if vals['SMA_100'] is not None else None,
                    SMA_150=round(float(vals['SMA_150']) if isinstance(vals['SMA_150'], (float, int)) else (float(vals['SMA_150'].replace(',', '')) if vals['SMA_150'] not in [None, 'None'] else 0), 2) if vals['SMA_150'] is not None else None,
                    SMA_200=round(float(vals['SMA_200']) if isinstance(vals['SMA_200'], (float, int)) else (float(vals['SMA_200'].replace(',', '')) if vals['SMA_200'] not in [None, 'None'] else 0), 2) if vals['SMA_200'] is not None else None,
                    ema=round(float(vals['EMA']) if isinstance(vals['EMA'], (float, int)) else (float(vals['EMA'].replace(',', '')) if vals['EMA'] not in [None, 'None'] else 0), 2) if vals['EMA'] is not None else None,
                    rsi=round(float(vals['RSI']) if isinstance(vals['RSI'], (float, int)) else (float(vals['RSI'].replace(',', '')) if vals['RSI'] not in [None, 'None'] else 0), 2) if vals['RSI'] is not None else None
                )
            )

        # Сохраняем все данные в базе данных
        StockData.objects.bulk_create(final_table_in_db)

    return final_table
