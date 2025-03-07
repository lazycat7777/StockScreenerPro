from screener_daily_USA.models import Stock_Data_Overview

def get_symbols_and_exchanges():
    return [
        (symbol.split(':')[1], exchange) if ':' in symbol else (symbol, exchange)
        for symbol, exchange in Stock_Data_Overview.objects.values_list('symbol', 'exchange')
    ]

symbols_and_exchanges = get_symbols_and_exchanges()


# from django.db import connections


# with connections['tradingview_data_db'].cursor() as cursor:
#     cursor.execute("SELECT symbol FROM stock_data_overview")
#     rows = cursor.fetchall()
    
#     # Обработка и преобразование данных
#     symbols_and_exchanges = []
#     for row in rows:
#         full_symbol = row[0]
#         if ':' in full_symbol:  # Проверка, что символ содержит ':'
#             exchange, symbol = full_symbol.split(':')
#             symbols_and_exchanges.append((symbol, exchange))



# symbols_and_exchanges = [
#     ('AAM', 'NYSE'),
#     ('BKV', 'NASDAQ'),
#     ('CBNA', 'NASDAQ'),
#     ('BKNG', 'NASDAQ'),
#     ('MELI', 'NASDAQ'),
#     ('ORLY', 'NASDAQ'),
#     ('REAX', 'NASDAQ'),
#     ('AAPL', 'NASDAQ'),
#     ('GOOGL', 'NASDAQ'),
#     ('BVS', 'NASDAQ'),
#     ('LOVE', 'NASDAQ'),
#     ('TREE', 'NASDAQ'),
#     ('SLQT', 'NYSE'),
#     ('RVMD', 'NASDAQ'),
#     ('SLNO', 'NASDAQ'),
#     ('COMP', 'NYSE'),
#     ('SGHT', 'NASDAQ'),
# ]
