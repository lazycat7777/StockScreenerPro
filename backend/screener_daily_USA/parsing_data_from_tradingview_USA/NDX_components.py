import requests
from django.db import transaction
from ..models import NDX_Components 

URL = 'https://scanner.tradingview.com/global/scan?label-product=symbols-components'
HEADERS = {
    'accept': 'application/json',
    'content-type': 'application/json; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'origin': 'https://www.tradingview.com',
    'referer': 'https://www.tradingview.com/',
}

payload = {
    "columns": [
        "name", "description", "logoid", "update_mode", "type", "typespecs", 
        "market_cap_basic", "fundamental_currency_code", "close", "pricescale", 
        "minmov", "fractional", "minmove2", "currency", "change", "volume", 
        "relative_volume_10d_calc", "price_earnings_ttm", "earnings_per_share_diluted_ttm",
        "earnings_per_share_diluted_yoy_growth_ttm", "dividends_yield_current", 
        "sector.tr", "market", "sector", "recommendation_mark"
    ],
    "ignore_unknown_fields": False,
    "options": {"lang": "en"},
    "preset": "index_components_market_pages",
    "range": [0, 1000],
    "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc", "nullsFirst": False},
    "symbols": {"symbolset": ["SYML:NASDAQ;NDX"]}
}

def get_stock_data():
    response = requests.post(URL, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']  
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def NDX_components_get_stock_data():
    stock_data = get_stock_data()

    if stock_data:
        stock_objects = [
            NDX_Components(
                symbol=stock.get('s'),
                ndx_components='NASDAQ 100',
                name=stock.get('d')[0] if len(stock['d']) > 0 else None,
                description=stock.get('d')[1] if len(stock['d']) > 1 else None,
                logoid=stock.get('d')[2] if len(stock['d']) > 2 else None,
                update_mode=stock.get('d')[3] if len(stock['d']) > 3 else None,
                type=stock.get('d')[4] if len(stock['d']) > 4 else None,
                typespecs=stock.get('d')[5] if len(stock['d']) > 5 else None,
                market_cap_basic=stock.get('d')[6] if len(stock['d']) > 6 else None,
                fundamental_currency_code=stock.get('d')[7] if len(stock['d']) > 7 else None,
                close=stock.get('d')[8] if len(stock['d']) > 8 else None,
                pricescale=stock.get('d')[9] if len(stock['d']) > 9 else None,
                minmov=stock.get('d')[10] if len(stock['d']) > 10 else None,
                fractional=stock.get('d')[11] if len(stock['d']) > 11 else None,
                minmove2=stock.get('d')[12] if len(stock['d']) > 12 else None,
                currency=stock.get('d')[13] if len(stock['d']) > 13 else None,
                change=stock.get('d')[14] if len(stock['d']) > 14 else None,
                volume=stock.get('d')[15] if len(stock['d']) > 15 else None,
                relative_volume_10d_calc=stock.get('d')[16] if len(stock['d']) > 16 else None,
                price_earnings_ttm=stock.get('d')[17] if len(stock['d']) > 17 else None,
                earnings_per_share_diluted_ttm=stock.get('d')[18] if len(stock['d']) > 18 else None,
                earnings_per_share_diluted_yoy_growth_ttm=stock.get('d')[19] if len(stock['d']) > 19 else None,
                dividends_yield_current=stock.get('d')[20] if len(stock['d']) > 20 else None,
                sector_tr=stock.get('d')[21] if len(stock['d']) > 21 else None,
                market=stock.get('d')[22] if len(stock['d']) > 22 else None,
                sector=stock.get('d')[23] if len(stock['d']) > 23 else None,
                recommendation_mark=stock.get('d')[24] if len(stock['d']) > 24 else None,
            ) for stock in stock_data
        ]

        NDX_Components.objects.all().delete()  

        with transaction.atomic():  
            NDX_Components.objects.bulk_create(stock_objects)

        print("Данные NDX_Components успешно сохранены в базу данных.")
    else:
        print("Не удалось получить данные акций.")
