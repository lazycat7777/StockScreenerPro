from screener_daily_USA.parsing_data_from_tradingview_USA.SPX_components import get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные SPX_Components успешно сохранены в базу данных.'))