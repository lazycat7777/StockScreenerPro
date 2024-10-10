import pandas as pd

others_list = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt'
nasdaq_list = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'


def symbols_nyse():
    other = pd.read_csv(others_list, sep='|')
    company_nyse = other[other['Exchange'] == 'N'][['ACT Symbol', 'Security Name']]
    company_nyse = company_nyse.reset_index(drop=True)
    company_nyse = company_nyse.rename(columns={'ACT Symbol': 'Symbol'})
    return company_nyse


def symbols_nasdaq():
    nasdaq = pd.read_csv(nasdaq_list, sep='|')
    nasdaq_normal = nasdaq[nasdaq['Financial Status'] == 'N']
    nasdaq_normal = nasdaq_normal[nasdaq_normal['Test Issue'] == 'N']
    company_nasdaq = nasdaq_normal[nasdaq_normal['ETF'] == 'N'][['Symbol', 'Security Name']]
    company_nasdaq = company_nasdaq.reset_index(drop=True)
    return company_nasdaq


def symbols_all():
    company_nyse = symbols_nyse()
    company_nasdaq = symbols_nasdaq()
    # Добавляем столбец 'Market'
    company_nyse['Market'] = 'NYSE'
    company_nasdaq['Market'] = 'NASDAQ'

    # Объединяем данные NYSE и NASDAQ
    all_companies = pd.concat([company_nyse, company_nasdaq], ignore_index=True, sort=False)

    # Создаем список кортежей (Symbol, Exchange)
    symbols_and_exchanges = list(zip(all_companies['Symbol'], all_companies['Market']))

    return symbols_and_exchanges


# Вызовите функцию и получите результат
result_parser_of_symbols = symbols_all()
# print(result_parser_of_symbols)



# результат готов
