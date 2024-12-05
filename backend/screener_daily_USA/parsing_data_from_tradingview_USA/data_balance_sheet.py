import requests
from ..models import Stock_Data_Balance_Sheet 
from django.db import transaction

URL = 'https://scanner.tradingview.com/america/scan?label-product=markets-screener'
HEADERS = {
    'authority': 'scanner.tradingview.com',
    'accept': 'application/json',
    'content-type': 'application/json; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'origin': 'https://www.tradingview.com',
    'referer': 'https://www.tradingview.com/',
}

payload = {
    "columns": [
        "name", "description", "logoid", "update_mode", "type", "typespecs",
        "total_assets_fq", "fundamental_currency_code", "total_current_assets_fq",
        "cash_n_short_term_invest_fq", "total_liabilities_fq", "total_debt_fq",
        "net_debt_fq", "total_equity_fq", "current_ratio_fq", "quick_ratio_fq",
        "debt_to_equity_fq", "cash_n_short_term_invest_to_total_debt_fq"
    ],
    "ignore_unknown_fields": False,
    "options": {
        "lang": "en"
    },
    "preset": "all_stocks",
    "range": [0, 9999],
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
        return data['data']  
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def data_balance_sheet_get_stock_data():
    stock_data = get_stock_data()

    if stock_data:
        stock_objects = []
        for stock in stock_data:
            stock_objects.append(
                Stock_Data_Balance_Sheet(
                    symbol=stock.get('s'),
                    name=stock.get('d')[0] if len(stock['d']) > 0 else None,
                    exchange=stock.get('s').split(':')[0],
                    description=stock.get('d')[1] if len(stock['d']) > 1 else None,
                    logoid=stock.get('d')[2] if len(stock['d']) > 2 else None,
                    update_mode=stock.get('d')[3] if len(stock['d']) > 3 else None,
                    type=stock.get('d')[4] if len(stock['d']) > 4 else None,
                    typespecs=stock.get('d')[5] if len(stock['d']) > 5 else None,
                    total_assets_fq=stock.get('d')[6] if len(stock['d']) > 6 else None,
                    fundamental_currency_code=stock.get('d')[7] if len(stock['d']) > 7 else None,
                    total_current_assets_fq=stock.get('d')[8] if len(stock['d']) > 8 else None,
                    cash_n_short_term_invest_fq=stock.get('d')[9] if len(stock['d']) > 9 else None,
                    total_liabilities_fq=stock.get('d')[10] if len(stock['d']) > 10 else None,
                    total_debt_fq=stock.get('d')[11] if len(stock['d']) > 11 else None,
                    net_debt_fq=stock.get('d')[12] if len(stock['d']) > 12 else None,
                    total_equity_fq=stock.get('d')[13] if len(stock['d']) > 13 else None,
                    current_ratio_fq=stock.get('d')[14] if len(stock['d']) > 14 else None,
                    quick_ratio_fq=stock.get('d')[15] if len(stock['d']) > 15 else None,
                    debt_to_equity_fq=stock.get('d')[16] if len(stock['d']) > 16 else None,
                    cash_n_short_term_invest_to_total_debt_fq=stock.get('d')[17] if len(stock['d']) > 17 else None,
                )
            )
        
        Stock_Data_Balance_Sheet.objects.all().delete()

        with transaction.atomic(): 
            Stock_Data_Balance_Sheet.objects.bulk_create(stock_objects)

        print("Данные Stock_Data_Balance_Sheet успешно сохранены в базу данных.")
    else:
        print("Не удалось получить данные акций.")
