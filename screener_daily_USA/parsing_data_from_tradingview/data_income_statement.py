import requests
import pandas as pd
import sqlite3

# Устанавливаем URL и заголовки
URL = 'https://scanner.tradingview.com/america/scan?label-product=markets-screener'
HEADERS = {
    'authority': 'scanner.tradingview.com',
    'accept': 'application/json',
    'content-type': 'application/json; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'origin': 'https://www.tradingview.com',
    'referer': 'https://www.tradingview.com/',
}

# Тело запроса с параметрами
payload = {
    "columns": [
        "name", "description", "logoid", "update_mode", "type", "typespecs",
        "total_revenue_ttm", "fundamental_currency_code", "total_revenue_yoy_growth_ttm",
        "gross_profit_ttm", "oper_income_ttm", "net_income_ttm",
        "ebitda_ttm", "earnings_per_share_diluted_ttm", "earnings_per_share_diluted_yoy_growth_ttm"
    ],
    "ignore_unknown_fields": False,
    "options": {
        "lang": "en"
    },
    "preset": "all_stocks",
    "range": [0, 999999],  # Оставляем старый диапазон
    "sort": {
        "sortBy": "name",
        "sortOrder": "asc",
        "nullsFirst": False
    },
    "filter": [
        {"left": "exchange", "operation": "in_range", "right": ["AMEX", "NASDAQ", "NYSE"]},
        {"left": "is_primary", "operation": "equal", "right": True},
        {"left": "typespecs", "operation": "has", "right": "common"},
        {"left": "typespecs", "operation": "has_none_of", "right": "preferred"},
        {"left": "type", "operation": "equal", "right": "stock"}
    ],
    "symbols": {
        "query": {
            "types": ["stock", "fund", "dr", "structured"]
        }
    }
}

def get_stock_data():
    response = requests.post(URL, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']  # Возвращаем данные акций
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Получаем данные
stock_data = get_stock_data()

if stock_data:
    # Преобразуем данные в DataFrame
    df = pd.DataFrame([{
        'symbol': stock.get('s'),
        'name': stock.get('d')[0] if len(stock['d']) > 0 else None,
        'exchange': stock.get('s').split(':')[0],  # Извлекаем текст до знака ':'
        'description': stock.get('d')[1] if len(stock['d']) > 1 else None,
        'logoid': stock.get('d')[2] if len(stock['d']) > 2 else None,
        'update_mode': stock.get('d')[3] if len(stock['d']) > 3 else None,
        'type': stock.get('d')[4] if len(stock['d']) > 4 else None,
        'typespecs': stock.get('d')[5] if len(stock['d']) > 5 else None,
        'total_revenue_ttm': stock.get('d')[6] if len(stock['d']) > 6 else None,
        'fundamental_currency_code': stock.get('d')[7] if len(stock['d']) > 7 else None,
        'total_revenue_yoy_growth_ttm': stock.get('d')[8] if len(stock['d']) > 8 else None,
        'gross_profit_ttm': stock.get('d')[9] if len(stock['d']) > 9 else None,
        'oper_income_ttm': stock.get('d')[10] if len(stock['d']) > 10 else None,
        'net_income_ttm': stock.get('d')[11] if len(stock['d']) > 11 else None,
        'ebitda_ttm': stock.get('d')[12] if len(stock['d']) > 12 else None,
        'earnings_per_share_diluted_ttm': stock.get('d')[13] if len(stock['d']) > 13 else None,
        'earnings_per_share_diluted_yoy_growth_ttm': stock.get('d')[14] if len(stock['d']) > 14 else None,
    } for stock in stock_data])
    
    # Преобразуем типы данных
    df['typespecs'] = df['typespecs'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    
    # Создаем соединение с SQLite базой данных
    conn = sqlite3.connect('tradingview_data.db')
    
    # Сохраняем данные в таблицу 'stock_data_income_statement'
    df.to_sql('stock_data_income_statement', conn, if_exists='replace', index=False)
    
    print("Данные успешно сохранены в базу данных SQLite.")
    
    # Закрываем соединение
    conn.close()
else:
    print("Не удалось получить данные акций.")
