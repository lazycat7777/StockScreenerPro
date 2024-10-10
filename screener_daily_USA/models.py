from django.db import models
# Create your models here.


class StockData(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    exchange = models.CharField(max_length=255)
    price = models.FloatField()
    ADR_percent = models.FloatField()
    SMA_10 = models.FloatField()
    SMA_20 = models.FloatField()
    SMA_50 = models.FloatField()
    SMA_100 = models.FloatField()
    SMA_150 = models.FloatField()
    SMA_200 = models.FloatField()
    ema = models.FloatField()
    rsi = models.FloatField()

    class Meta:
        app_label = 'screener_daily_USA' 
        db_table = 'stock_data'

