import sqlite3
import pandas as pd
from django.db import connection
from ..models import Stock_Data_Overview, Stock_Data_Performance, Stock_Data_Valuation

# Функция для конвертации QuerySet в DataFrame
def queryset_to_dataframe(queryset, columns):
    with connection.cursor() as cursor:
        cursor.execute(str(queryset.query))
        rows = cursor.fetchall()
    return pd.DataFrame(rows, columns=columns)


def merge_tables():
    # Stock_Data_Overview
    overview_columns = [
        'symbol', 'name', 'exchange', 'description', 'type', 'typespecs', 'close',
        'currency', 'change', 'volume', 'relative_volume_10d_calc',
        'market_cap_basic', 'fundamental_currency_code', 'price_earnings_ttm',
        'earnings_per_share_diluted_ttm', 'earnings_per_share_diluted_yoy_growth_ttm',
        'dividends_yield_current', 'sector_tr', 'market', 'sector'
    ]
    overview_data = queryset_to_dataframe(
        Stock_Data_Overview.objects.all().only(*overview_columns), 
        overview_columns
    )

    # Stock_Data_Performance
    performance_columns = [
        'perf_w', 'perf_1m', 'perf_3m', 'perf_6m', 'perf_ytd', 'perf_y', 
        'perf_5y', 'perf_10y', 'perf_all', 'volatility_w', 'volatility_m'
    ]
    performance_data = queryset_to_dataframe(
        Stock_Data_Performance.objects.all().only('symbol', *performance_columns), 
        ['symbol'] + performance_columns
    )

    # Stock_Data_Valuation
    valuation_columns = [
        'price_earnings_ttm', 'price_earnings_growth_ttm', 'price_sales_current',
        'price_book_fq', 'price_to_cash_f_operating_activities_ttm', 'price_free_cash_flow_ttm',
        'price_to_cash_ratio', 'enterprise_value_current', 'enterprise_value_to_revenue_ttm',
        'enterprise_value_to_ebit_ttm', 'enterprise_value_ebitda_ttm'
    ]
    valuation_data = queryset_to_dataframe(
        Stock_Data_Valuation.objects.all().only('symbol', *valuation_columns),
        ['symbol'] + valuation_columns
    )

    # left join по столбцу symbol для всех данных
    merged_data = pd.merge(overview_data, performance_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, valuation_data, on='symbol', how='left')

    with sqlite3.connect("merge_tables.db") as conn:
        merged_data.to_sql("merged_stock_data", conn, if_exists="replace", index=False)

    print("Данные успешно сохранены.")
