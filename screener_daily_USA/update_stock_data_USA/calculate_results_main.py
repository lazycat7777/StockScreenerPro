from .connecting_to_tradingview import get_new_data
from .indicators import calculate_indicators
from .symbols_and_exchanges_main import symbols_and_exchanges
from .connecting_to_tradingview import interval

from ..models import Stock_Data_Indicators
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
        'High_10',
        'High_20',
        'High_50',
        'High_100',
        'High_150',
        'High_200',
        'High_1Y',
        'Low_10',
        'Low_20',
        'Low_50',
        'Low_100',
        'Low_150',
        'Low_200',
        'Low_1Y'
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
                'High_10': indicators_dict['High_10'],
                'High_20': indicators_dict['High_20'],
                'High_50': indicators_dict['High_50'],
                'High_100': indicators_dict['High_100'],
                'High_150': indicators_dict['High_150'],
                'High_200': indicators_dict['High_200'],
                'High_1Y': indicators_dict['High_1Y'],
                'Low_10': indicators_dict['Low_10'],
                'Low_20': indicators_dict['Low_20'],
                'Low_50': indicators_dict['Low_50'],
                'Low_100': indicators_dict['Low_100'],
                'Low_150': indicators_dict['Low_150'],
                'Low_200': indicators_dict['Low_200'],
                'Low_1Y': indicators_dict['Low_1Y']
            })

    # После завершения цикла добавляем все результаты в таблицу
    if results:
        final_table = pd.concat([final_table, pd.DataFrame(results)], ignore_index=True)

    # Заменяем NaN на None перед сохранением в базу данных
    final_table = final_table.replace({np.nan: None})

    # Очистка таблицы в базе данных перед сохранением новых данных
    Stock_Data_Indicators.objects.all().delete()

    # Сохраняем данные в одном транзакционном блоке
    with transaction.atomic():
        final_table_in_db = []
        for vals in final_table.to_dict(orient='records'):
            final_table_in_db.append(
                Stock_Data_Indicators(
                    symbol=vals['Symbol'], 
                    ADR_percent=round(vals['ADR_percent'], 2) if vals['ADR_percent'] is not None else None,
                    SMA_10=round(vals['SMA_10'], 2) if vals['SMA_10'] is not None else None,
                    SMA_20=round(vals['SMA_20'], 2) if vals['SMA_20'] is not None else None,
                    SMA_50=round(vals['SMA_50'], 2) if vals['SMA_50'] is not None else None,
                    SMA_100=round(vals['SMA_100'], 2) if vals['SMA_100'] is not None else None,
                    SMA_150=round(vals['SMA_150'], 2) if vals['SMA_150'] is not None else None,
                    SMA_200=round(vals['SMA_200'], 2) if vals['SMA_200'] is not None else None,
                    high_10=round(vals['High_10'], 2) if vals['High_10'] is not None else None,
                    high_20=round(vals['High_20'], 2) if vals['High_20'] is not None else None,
                    high_50=round(vals['High_50'], 2) if vals['High_50'] is not None else None,
                    high_100=round(vals['High_100'], 2) if vals['High_100'] is not None else None,
                    high_150=round(vals['High_150'], 2) if vals['High_150'] is not None else None,
                    high_200=round(vals['High_200'], 2) if vals['High_200'] is not None else None,
                    high_1y=round(vals['High_1Y'], 2) if vals['High_1Y'] is not None else None,
                    low_10=round(vals['Low_10'], 2) if vals['Low_10'] is not None else None,
                    low_20=round(vals['Low_20'], 2) if vals['Low_20'] is not None else None,
                    low_50=round(vals['Low_50'], 2) if vals['Low_50'] is not None else None,
                    low_100=round(vals['Low_100'], 2) if vals['Low_100'] is not None else None,
                    low_150=round(vals['Low_150'], 2) if vals['Low_150'] is not None else None,
                    low_200=round(vals['Low_200'], 2) if vals['Low_200'] is not None else None,
                    low_1y=round(vals['Low_1Y'], 2) if vals['Low_1Y'] is not None else None,
                )
            )
        Stock_Data_Indicators.objects.bulk_create(final_table_in_db)
