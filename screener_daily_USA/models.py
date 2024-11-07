from django.db import models

class Stock_Merge_All_Tables(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)

    # Поля из Stock_Data_Overview
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    close = models.FloatField(null=True)
    currency = models.CharField(max_length=255, null=True)
    change = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    relative_volume_10d_calc = models.FloatField(null=True)
    market_cap_basic = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    price_earnings_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_yoy_growth_ttm = models.FloatField(null=True)
    dividends_yield_current = models.FloatField(null=True)
    sector_tr = models.CharField(max_length=255, null=True)
    market = models.CharField(max_length=255, null=True)
    sector = models.CharField(max_length=255, null=True)

    # Поля из Stock_Data_Performance
    perf_w = models.FloatField(null=True)
    perf_1m = models.FloatField(null=True)
    perf_3m = models.FloatField(null=True)
    perf_6m = models.FloatField(null=True)
    perf_ytd = models.FloatField(null=True)
    perf_y = models.FloatField(null=True)
    perf_5y = models.FloatField(null=True)
    perf_10y = models.FloatField(null=True)
    perf_all = models.FloatField(null=True)
    volatility_w = models.FloatField(null=True)
    volatility_m = models.FloatField(null=True)

    # Поля из Stock_Data_Valuation
    perf_1y_market_cap = models.FloatField(null=True)
    price_earnings_growth_ttm = models.FloatField(null=True)
    price_sales_current = models.FloatField(null=True)
    price_book_fq = models.FloatField(null=True)
    price_to_cash_f_operating_activities_ttm = models.FloatField(null=True)
    price_free_cash_flow_ttm = models.FloatField(null=True)
    price_to_cash_ratio = models.FloatField(null=True)
    enterprise_value_current = models.FloatField(null=True)
    enterprise_value_to_revenue_ttm = models.FloatField(null=True)
    enterprise_value_to_ebit_ttm = models.FloatField(null=True)
    enterprise_value_ebitda_ttm = models.FloatField(null=True)

    # Поля из Stock_Data_Dividends
    dps_common_stock_prim_issue_fy = models.FloatField(null=True)
    dps_common_stock_prim_issue_fq = models.FloatField(null=True)
    dividends_yield = models.FloatField(null=True)
    dividend_payout_ratio_ttm = models.FloatField(null=True)
    dps_common_stock_prim_issue_yoy_growth_fy = models.FloatField(null=True)
    continuous_dividend_payout = models.FloatField(null=True)
    continuous_dividend_growth = models.FloatField(null=True)

    # Поля из Stock_Data_Profitability
    gross_margin_ttm = models.FloatField(null=True)
    operating_margin_ttm = models.FloatField(null=True)
    pre_tax_margin_ttm = models.FloatField(null=True)
    net_margin_ttm = models.FloatField(null=True)
    free_cash_flow_margin_ttm = models.FloatField(null=True)
    return_on_assets_fq = models.FloatField(null=True)
    return_on_equity_fq = models.FloatField(null=True)
    return_on_invested_capital_fq = models.FloatField(null=True)
    research_and_dev_ratio_ttm = models.FloatField(null=True)
    sell_gen_admin_exp_other_ratio_ttm = models.FloatField(null=True)

    # Поля из Stock_Data_Income_Statement
    total_revenue_ttm = models.FloatField(null=True)
    total_revenue_yoy_growth_ttm = models.FloatField(null=True)
    gross_profit_ttm = models.FloatField(null=True)
    oper_income_ttm = models.FloatField(null=True)
    net_income_ttm = models.FloatField(null=True)
    ebitda_ttm = models.FloatField(null=True)

    # Поля из Stock_Data_Balance_Sheet
    total_assets_fq = models.FloatField(null=True)
    total_current_assets_fq = models.FloatField(null=True)
    cash_n_short_term_invest_fq = models.FloatField(null=True)
    total_liabilities_fq = models.FloatField(null=True)
    total_debt_fq = models.FloatField(null=True)
    net_debt_fq = models.FloatField(null=True)
    total_equity_fq = models.FloatField(null=True)
    current_ratio_fq = models.FloatField(null=True)
    quick_ratio_fq = models.FloatField(null=True)
    debt_to_equity_fq = models.FloatField(null=True)
    cash_n_short_term_invest_to_total_debt_fq = models.FloatField(null=True)

    # Поля из Stock_Data_Cash_Flow
    cash_f_operating_activities_ttm = models.FloatField(null=True)
    cash_f_investing_activities_ttm = models.FloatField(null=True)
    cash_f_financing_activities_ttm = models.FloatField(null=True)
    free_cash_flow_ttm = models.FloatField(null=True)
    capital_expenditures_ttm = models.FloatField(null=True)

    # Поля из SPX_Components и NDX_Components
    spx_components = models.CharField(max_length=255, null=True)
    ndx_components = models.CharField(max_length=255, null=True)

    # Поля из Stock_Data_Indicators
    ADR_percent = models.FloatField(null=True)
    SMA_10 = models.FloatField(null=True)
    SMA_20 = models.FloatField(null=True)
    SMA_50 = models.FloatField(null=True)
    SMA_100 = models.FloatField(null=True)
    SMA_150 = models.FloatField(null=True)
    SMA_200 = models.FloatField(null=True)
    high_10 = models.FloatField(null=True)
    high_20 = models.FloatField(null=True)
    high_50 = models.FloatField(null=True)
    high_100 = models.FloatField(null=True)
    high_150 = models.FloatField(null=True)
    high_200 = models.FloatField(null=True)
    high_1y = models.FloatField(null=True)
    low_10 = models.FloatField(null=True)
    low_20 = models.FloatField(null=True)
    low_50 = models.FloatField(null=True)
    low_100 = models.FloatField(null=True)
    low_150 = models.FloatField(null=True)
    low_200 = models.FloatField(null=True)
    low_1y = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_merge_all_tables_USA'


class Stock_Data_Indicators(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    ADR_percent = models.FloatField(null=True)
    SMA_10 = models.FloatField(null=True)
    SMA_20 = models.FloatField(null=True)
    SMA_50 = models.FloatField(null=True)
    SMA_100 = models.FloatField(null=True)
    SMA_150 = models.FloatField(null=True)
    SMA_200 = models.FloatField(null=True) 
    high_10 = models.FloatField(null=True)
    high_20 = models.FloatField(null=True)
    high_50 = models.FloatField(null=True)
    high_100 = models.FloatField(null=True)
    high_150 = models.FloatField(null=True)
    high_200 = models.FloatField(null=True)
    high_1y = models.FloatField(null=True)
    low_10 = models.FloatField(null=True)
    low_20 = models.FloatField(null=True)
    low_50 = models.FloatField(null=True)
    low_100 = models.FloatField(null=True)
    low_150 = models.FloatField(null=True)
    low_200 = models.FloatField(null=True)
    low_1y = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_indicators_USA'


class Stock_Data_Balance_Sheet(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)  
    exchange = models.CharField(max_length=255, null=True)  
    description = models.CharField(max_length=255, null=True)  
    logoid = models.CharField(max_length=255, null=True)  
    update_mode = models.CharField(max_length=255, null=True)  
    type = models.CharField(max_length=50, null=True)  
    typespecs = models.CharField(max_length=255, null=True)  
    total_assets_fq = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    total_current_assets_fq = models.FloatField(null=True)
    cash_n_short_term_invest_fq = models.FloatField(null=True)
    total_liabilities_fq = models.FloatField(null=True)
    total_debt_fq = models.FloatField(null=True)
    net_debt_fq = models.FloatField(null=True)
    total_equity_fq = models.FloatField(null=True)
    current_ratio_fq = models.FloatField(null=True)
    quick_ratio_fq = models.FloatField(null=True)
    debt_to_equity_fq = models.FloatField(null=True)
    cash_n_short_term_invest_to_total_debt_fq = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'  
        db_table = 'stock_data_balance_sheet_USA'  

class Stock_Data_Cash_Flow(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=50, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    cash_f_operating_activities_ttm = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    cash_f_investing_activities_ttm = models.FloatField(null=True)
    cash_f_financing_activities_ttm = models.FloatField(null=True)
    free_cash_flow_ttm = models.FloatField(null=True)
    capital_expenditures_ttm = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'  
        db_table = 'stock_data_cash_flow_USA'  


class Stock_Data_Dividends(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    dps_common_stock_prim_issue_fy = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    dps_common_stock_prim_issue_fq = models.FloatField(null=True)
    dividends_yield_current = models.FloatField(null=True)
    dividends_yield = models.FloatField(null=True)
    dividend_payout_ratio_ttm = models.FloatField(null=True)
    dps_common_stock_prim_issue_yoy_growth_fy = models.FloatField(null=True)
    continuous_dividend_payout = models.FloatField(null=True)
    continuous_dividend_growth = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'  
        db_table = 'stock_data_dividends_USA' 


class Stock_Data_Income_Statement(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    total_revenue_ttm = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    total_revenue_yoy_growth_ttm = models.FloatField(null=True)
    gross_profit_ttm = models.FloatField(null=True)
    oper_income_ttm = models.FloatField(null=True)
    net_income_ttm = models.FloatField(null=True)
    ebitda_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_yoy_growth_ttm = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_income_statement_USA'


class Stock_Data_Overview(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    close = models.FloatField(null=True)
    pricescale = models.FloatField(null=True)
    minmov = models.FloatField(null=True)
    fractional = models.CharField(max_length=255, null=True)
    minmove2 = models.FloatField(null=True)
    currency = models.CharField(max_length=255, null=True)
    change = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    relative_volume_10d_calc = models.FloatField(null=True)
    market_cap_basic = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    price_earnings_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_yoy_growth_ttm = models.FloatField(null=True)
    dividends_yield_current = models.FloatField(null=True)
    sector_tr = models.CharField(max_length=255, null=True)
    market = models.CharField(max_length=255, null=True)
    sector = models.CharField(max_length=255, null=True)
    recommendation_mark = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_overview_USA'

class Stock_Data_Performance(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)  
    close = models.FloatField(null=True)
    pricescale = models.FloatField(null=True)
    minmov = models.FloatField(null=True)
    fractional = models.CharField(max_length=255, null=True)  
    minmove2 = models.FloatField(null=True)
    currency = models.CharField(max_length=255, null=True)
    change = models.FloatField(null=True)
    perf_w = models.FloatField(null=True)
    perf_1m = models.FloatField(null=True)
    perf_3m = models.FloatField(null=True)
    perf_6m = models.FloatField(null=True)
    perf_ytd = models.FloatField(null=True)
    perf_y = models.FloatField(null=True)
    perf_5y = models.FloatField(null=True)
    perf_10y = models.FloatField(null=True)
    perf_all = models.FloatField(null=True)
    volatility_w = models.FloatField(null=True)
    volatility_m = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_performance_USA'


class Stock_Data_Profitability(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    gross_margin_ttm = models.FloatField(null=True)
    operating_margin_ttm = models.FloatField(null=True)
    pre_tax_margin_ttm = models.FloatField(null=True)
    net_margin_ttm = models.FloatField(null=True)
    free_cash_flow_margin_ttm = models.FloatField(null=True)
    return_on_assets_fq = models.FloatField(null=True)
    return_on_equity_fq = models.FloatField(null=True)
    return_on_invested_capital_fq = models.FloatField(null=True)
    research_and_dev_ratio_ttm = models.FloatField(null=True)
    sell_gen_admin_exp_other_ratio_ttm = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_profitability_USA'


class Stock_Data_Valuation(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    exchange = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    market_cap_basic = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    perf_1y_market_cap = models.FloatField(null=True)
    price_earnings_ttm = models.FloatField(null=True)
    price_earnings_growth_ttm = models.FloatField(null=True)
    price_sales_current = models.FloatField(null=True)
    price_book_fq = models.FloatField(null=True)
    price_to_cash_f_operating_activities_ttm = models.FloatField(null=True)
    price_free_cash_flow_ttm = models.FloatField(null=True)
    price_to_cash_ratio = models.FloatField(null=True)
    enterprise_value_current = models.FloatField(null=True)
    enterprise_value_to_revenue_ttm = models.FloatField(null=True)
    enterprise_value_to_ebit_ttm = models.FloatField(null=True)
    enterprise_value_ebitda_ttm = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_data_valuation_USA'


class NDX_Components(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    ndx_components = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    market_cap_basic = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    close = models.FloatField(null=True)
    pricescale = models.FloatField(null=True)
    minmov = models.FloatField(null=True)
    fractional = models.CharField(max_length=255, null=True)
    minmove2 = models.FloatField(null=True)
    currency = models.CharField(max_length=255, null=True)
    change = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    relative_volume_10d_calc = models.FloatField(null=True)
    price_earnings_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_yoy_growth_ttm = models.FloatField(null=True)
    dividends_yield_current = models.FloatField(null=True)
    sector_tr = models.CharField(max_length=255, null=True)
    market = models.CharField(max_length=255, null=True)
    sector = models.CharField(max_length=255, null=True)
    recommendation_mark = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'screener_daily_USA'
        db_table = 'stock_NDX_components_USA'


class SPX_Components(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    spx_components = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    logoid = models.CharField(max_length=255, null=True)
    update_mode = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    typespecs = models.CharField(max_length=255, null=True)
    market_cap_basic = models.FloatField(null=True)
    fundamental_currency_code = models.CharField(max_length=255, null=True)
    close = models.FloatField(null=True)
    pricescale = models.FloatField(null=True)
    minmov = models.FloatField(null=True)
    fractional = models.CharField(max_length=255, null=True)
    minmove2 = models.FloatField(null=True)
    currency = models.CharField(max_length=255, null=True)
    change = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    relative_volume_10d_calc = models.FloatField(null=True)
    price_earnings_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_ttm = models.FloatField(null=True)
    earnings_per_share_diluted_yoy_growth_ttm = models.FloatField(null=True)
    dividends_yield_current = models.FloatField(null=True)
    sector_tr = models.CharField(max_length=255, null=True)
    market = models.CharField(max_length=255, null=True)
    sector = models.CharField(max_length=255, null=True)
    recommendation_mark = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'screener_daily_USA' 
        db_table = 'stock_SPX_components_USA' 
