from django.db import models
# Create your models here.


class StockData(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    exchange = models.CharField(max_length=255)
    price = models.FloatField(null=True)
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
        db_table = 'stock_data'
