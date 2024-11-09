import time
from datetime import timedelta
from screener_daily_USA.parsing_data_from_tradingview_USA.data_overview import data_overview_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_performance import data_performance_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_valuation import data_valuation_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_dividends import data_dividends_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_profitability import data_profitability_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_income_statement import data_income_statement_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_balance_sheet import data_balance_sheet_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.data_cash_flow import data_cash_flow_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.SPX_components import SPX_components_get_stock_data
from screener_daily_USA.parsing_data_from_tradingview_USA.NDX_components import NDX_components_get_stock_data
from screener_daily_USA.update_stock_data_USA.calculate_results_main import calculate_and_aggregate_results
from screener_daily_USA.update_stock_data_USA.merge_all_tables import merge_tables, save_merge_tables_to_db

from screener_website.celery_app import app

@app.task
def calculate_results_USA():
    start_time = time.time()  

    data_overview_get_stock_data()
    data_performance_get_stock_data()
    data_valuation_get_stock_data()
    data_dividends_get_stock_data()
    data_profitability_get_stock_data()
    data_income_statement_get_stock_data()
    data_balance_sheet_get_stock_data()
    data_cash_flow_get_stock_data()
    SPX_components_get_stock_data()
    NDX_components_get_stock_data()
    calculate_and_aggregate_results()

    merged_data = merge_tables()
    save_merge_tables_to_db(merged_data)

    end_time = time.time()  
    elapsed_time = end_time - start_time  
    elapsed_time_formatted = str(timedelta(seconds=elapsed_time))
    print(f'Селери таска завершена, данные акций США обновлены. Время выполнения: {elapsed_time_formatted}')
