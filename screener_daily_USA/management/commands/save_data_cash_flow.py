from screener_daily_USA.parsing_data_from_tradingview_USA.data_cash_flow import data_cash_flow_get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_cash_flow_get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Cash_Flow успешно сохранены в базу данных.'))