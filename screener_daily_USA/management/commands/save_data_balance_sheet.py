from screener_daily_USA.parsing_data_from_tradingview.data_balance_sheet import get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Balance_Sheet успешно сохранены в базу данных.'))