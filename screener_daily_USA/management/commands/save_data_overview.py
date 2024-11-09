from screener_daily_USA.parsing_data_from_tradingview_USA.data_overview import data_overview_get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_overview_get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Overview успешно сохранены в базу данных.'))