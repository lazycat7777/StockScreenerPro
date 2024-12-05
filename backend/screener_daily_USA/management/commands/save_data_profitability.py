from screener_daily_USA.parsing_data_from_tradingview_USA.data_profitability import data_profitability_get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_profitability_get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Profitability успешно сохранены в базу данных.'))