import pandas as pd
import numpy as np
from django.db import connection
from ..models import (
    Stock_Data_Overview,
    Stock_Data_Performance,
    Stock_Data_Valuation,
    Stock_Data_Dividends,
    Stock_Data_Profitability,
    Stock_Data_Income_Statement,
    Stock_Data_Balance_Sheet,
    Stock_Data_Cash_Flow,
    SPX_Components,
    NDX_Components,
    Stock_Data_Indicators,
    Stock_Merge_All_Tables
)

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
        'perf_1y_market_cap', 'price_earnings_growth_ttm', 'price_sales_current',
        'price_book_fq', 'price_to_cash_f_operating_activities_ttm', 'price_free_cash_flow_ttm',
        'price_to_cash_ratio', 'enterprise_value_current', 'enterprise_value_to_revenue_ttm',
        'enterprise_value_to_ebit_ttm', 'enterprise_value_ebitda_ttm'
    ]
    valuation_data = queryset_to_dataframe(
        Stock_Data_Valuation.objects.all().only('symbol', *valuation_columns),
        ['symbol'] + valuation_columns
    )

    # Stock_Data_Dividends
    dividends_columns = [
        'dps_common_stock_prim_issue_fy', 'dps_common_stock_prim_issue_fq', 
        'dividends_yield', 'dividend_payout_ratio_ttm', 
        'dps_common_stock_prim_issue_yoy_growth_fy', 'continuous_dividend_payout', 
        'continuous_dividend_growth'
    ]
    dividends_data = queryset_to_dataframe(
        Stock_Data_Dividends.objects.all().only('symbol', *dividends_columns),
        ['symbol'] + dividends_columns
    )

    # Stock_Data_Profitability
    profitability_columns = [
        'gross_margin_ttm', 'operating_margin_ttm', 'pre_tax_margin_ttm', 'net_margin_ttm',
        'free_cash_flow_margin_ttm', 'return_on_assets_fq', 'return_on_equity_fq', 
        'return_on_invested_capital_fq', 'research_and_dev_ratio_ttm', 'sell_gen_admin_exp_other_ratio_ttm'
    ]
    profitability_data = queryset_to_dataframe(
        Stock_Data_Profitability.objects.all().only('symbol', *profitability_columns),
        ['symbol'] + profitability_columns
    )

    # Stock_Data_Income_Statement
    income_statement_columns = [
        'total_revenue_ttm', 'total_revenue_yoy_growth_ttm', 'gross_profit_ttm',
        'oper_income_ttm', 'net_income_ttm', 'ebitda_ttm'
    ]
    income_statement_data = queryset_to_dataframe(
        Stock_Data_Income_Statement.objects.all().only('symbol', *income_statement_columns),
        ['symbol'] + income_statement_columns
    )

    # Stock_Data_Balance_Sheet
    balance_sheet_columns = [
        'total_assets_fq', 'total_current_assets_fq', 'cash_n_short_term_invest_fq',
        'total_liabilities_fq', 'total_debt_fq', 'net_debt_fq', 'total_equity_fq',
        'current_ratio_fq', 'quick_ratio_fq', 'debt_to_equity_fq', 
        'cash_n_short_term_invest_to_total_debt_fq'
    ]
    balance_sheet_data = queryset_to_dataframe(
        Stock_Data_Balance_Sheet.objects.all().only('symbol', *balance_sheet_columns),
        ['symbol'] + balance_sheet_columns
    )

    # Stock_Data_Cash_Flow
    cash_flow_columns = [
        'cash_f_operating_activities_ttm', 'cash_f_investing_activities_ttm',
        'cash_f_financing_activities_ttm', 'free_cash_flow_ttm', 'capital_expenditures_ttm'
    ]
    cash_flow_data = queryset_to_dataframe(
        Stock_Data_Cash_Flow.objects.all().only('symbol', *cash_flow_columns),
        ['symbol'] + cash_flow_columns
    )

    # SPX_Components
    spx_components_data = queryset_to_dataframe(
        SPX_Components.objects.all().only('symbol', 'spx_components'),
        ['symbol', 'spx_components']
    )

    # NDX_Components
    ndx_components_data = queryset_to_dataframe(
        NDX_Components.objects.all().only('symbol', 'ndx_components'),
        ['symbol', 'ndx_components']
    )

    # Stock_Data_Indicators
    indicators_columns = [
        'ADR_percent', 'SMA_10', 'SMA_20', 'SMA_50', 'SMA_100', 'SMA_150', 'SMA_200', 
        'high_10', 'high_20', 'high_50', 'high_100', 'high_150', 'high_200', 
        'high_1y', 'low_10', 'low_20', 'low_50', 'low_100', 'low_150', 
        'low_200', 'low_1y'
    ]
    indicators_data = queryset_to_dataframe(
        Stock_Data_Indicators.objects.all().only('symbol', *indicators_columns),
        ['symbol'] + indicators_columns
    )

    # left join по столбцу symbol для всех данных
    merged_data = pd.merge(overview_data, performance_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, valuation_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, dividends_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, profitability_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, income_statement_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, balance_sheet_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, cash_flow_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, spx_components_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, ndx_components_data, on='symbol', how='left')
    merged_data = pd.merge(merged_data, indicators_data, on='symbol', how='left')
    
    merged_data = merged_data.replace({np.nan: None})

    return merged_data

def save_merge_tables_to_db(merged_data):
    Stock_Merge_All_Tables.objects.all().delete()

    records = [
        Stock_Merge_All_Tables(
            symbol=row['symbol'],
            name=row['name'],
            exchange=row['exchange'],
            description=row['description'],
            type=row['type'],
            typespecs=row['typespecs'],
            close=row['close'],
            currency=row['currency'],
            change=row['change'],
            volume=row['volume'],
            relative_volume_10d_calc=row['relative_volume_10d_calc'],
            market_cap_basic=row['market_cap_basic'],
            fundamental_currency_code=row['fundamental_currency_code'],
            price_earnings_ttm=row['price_earnings_ttm'],
            earnings_per_share_diluted_ttm=row['earnings_per_share_diluted_ttm'],
            earnings_per_share_diluted_yoy_growth_ttm=row['earnings_per_share_diluted_yoy_growth_ttm'],
            dividends_yield_current=row['dividends_yield_current'],
            sector_tr=row['sector_tr'],
            market=row['market'],
            sector=row['sector'],
            perf_w=row['perf_w'],
            perf_1m=row['perf_1m'],
            perf_3m=row['perf_3m'],
            perf_6m=row['perf_6m'],
            perf_ytd=row['perf_ytd'],
            perf_y=row['perf_y'],
            perf_5y=row['perf_5y'],
            perf_10y=row['perf_10y'],
            perf_all=row['perf_all'],
            volatility_w=row['volatility_w'],
            volatility_m=row['volatility_m'],
            perf_1y_market_cap=row['perf_1y_market_cap'],
            price_earnings_growth_ttm=row['price_earnings_growth_ttm'],
            price_sales_current=row['price_sales_current'],
            price_book_fq=row['price_book_fq'],
            price_to_cash_f_operating_activities_ttm=row['price_to_cash_f_operating_activities_ttm'],
            price_free_cash_flow_ttm=row['price_free_cash_flow_ttm'],
            price_to_cash_ratio=row['price_to_cash_ratio'],
            enterprise_value_current=row['enterprise_value_current'],
            enterprise_value_to_revenue_ttm=row['enterprise_value_to_revenue_ttm'],
            enterprise_value_to_ebit_ttm=row['enterprise_value_to_ebit_ttm'],
            enterprise_value_ebitda_ttm=row['enterprise_value_ebitda_ttm'],
            dps_common_stock_prim_issue_fy=row['dps_common_stock_prim_issue_fy'],
            dps_common_stock_prim_issue_fq=row['dps_common_stock_prim_issue_fq'],
            dividends_yield=row['dividends_yield'],
            dividend_payout_ratio_ttm=row['dividend_payout_ratio_ttm'],
            dps_common_stock_prim_issue_yoy_growth_fy=row['dps_common_stock_prim_issue_yoy_growth_fy'],
            continuous_dividend_payout=row['continuous_dividend_payout'],
            continuous_dividend_growth=row['continuous_dividend_growth'],
            gross_margin_ttm=row['gross_margin_ttm'],
            operating_margin_ttm=row['operating_margin_ttm'],
            pre_tax_margin_ttm=row['pre_tax_margin_ttm'],
            net_margin_ttm=row['net_margin_ttm'],
            free_cash_flow_margin_ttm=row['free_cash_flow_margin_ttm'],
            return_on_assets_fq=row['return_on_assets_fq'],
            return_on_equity_fq=row['return_on_equity_fq'],
            return_on_invested_capital_fq=row['return_on_invested_capital_fq'],
            research_and_dev_ratio_ttm=row['research_and_dev_ratio_ttm'],
            sell_gen_admin_exp_other_ratio_ttm=row['sell_gen_admin_exp_other_ratio_ttm'],
            total_revenue_ttm=row['total_revenue_ttm'],
            total_revenue_yoy_growth_ttm=row['total_revenue_yoy_growth_ttm'],
            gross_profit_ttm=row['gross_profit_ttm'],
            oper_income_ttm=row['oper_income_ttm'],
            net_income_ttm=row['net_income_ttm'],
            ebitda_ttm=row['ebitda_ttm'],
            total_assets_fq=row['total_assets_fq'],
            total_current_assets_fq=row['total_current_assets_fq'],
            cash_n_short_term_invest_fq=row['cash_n_short_term_invest_fq'],
            total_liabilities_fq=row['total_liabilities_fq'],
            total_debt_fq=row['total_debt_fq'],
            net_debt_fq=row['net_debt_fq'],
            total_equity_fq=row['total_equity_fq'],
            current_ratio_fq=row['current_ratio_fq'],
            quick_ratio_fq=row['quick_ratio_fq'],
            debt_to_equity_fq=row['debt_to_equity_fq'],
            cash_n_short_term_invest_to_total_debt_fq=row['cash_n_short_term_invest_to_total_debt_fq'],
            cash_f_operating_activities_ttm=row['cash_f_operating_activities_ttm'],
            cash_f_investing_activities_ttm=row['cash_f_investing_activities_ttm'],
            cash_f_financing_activities_ttm=row['cash_f_financing_activities_ttm'],
            free_cash_flow_ttm=row['free_cash_flow_ttm'],
            capital_expenditures_ttm=row['capital_expenditures_ttm'],
            spx_components=row['spx_components'],
            ndx_components=row['ndx_components'],
            ADR_percent=row['ADR_percent'],
            SMA_10=row['SMA_10'],
            SMA_20=row['SMA_20'],
            SMA_50=row['SMA_50'],
            SMA_100=row['SMA_100'],
            SMA_150=row['SMA_150'],
            SMA_200=row['SMA_200'],
            high_10=row['high_10'],
            high_20=row['high_20'],
            high_50=row['high_50'],
            high_100=row['high_100'],
            high_150=row['high_150'],
            high_200=row['high_200'],
            high_1y=row['high_1y'],
            low_10=row['low_10'],
            low_20=row['low_20'],
            low_50=row['low_50'],
            low_100=row['low_100'],
            low_150=row['low_150'],
            low_200=row['low_200'],
            low_1y=row['low_1y']
        )
        for _, row in merged_data.iterrows()
    ]

    Stock_Merge_All_Tables.objects.bulk_create(records, batch_size=1000)

    print("Данные Stock_Merge_All_Tables сохранены.")