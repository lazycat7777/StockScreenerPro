from screener_daily_USA.parsing_data_from_tradingview_USA.data_dividends import data_dividends_get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_dividends_get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Dividends успешно сохранены в базу данных.'))