from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    ADR_percent = models.FloatField(null=True)
    SMA_10 = models.FloatField(null=True)
    SMA_20 = models.FloatField(null=True)
    SMA_50 = models.FloatField(null=True)
    SMA_100 = models.FloatField(null=True)
    SMA_150 = models.FloatField(null=True)
    SMA_200 = models.FloatField(null=True)
    ema = models.FloatField(null=True)
    rsi = models.FloatField(null=True)

    class Meta:
        app_label = 'screener_daily_USA' 
        db_table = 'stock_data_indicators'


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
        db_table = 'stock_data_balance_sheet'  

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
        db_table = 'stock_data_cash_flow'  


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
        db_table = 'stock_data_dividends' 
