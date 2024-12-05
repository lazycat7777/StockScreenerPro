from screener_daily_USA.parsing_data_from_tradingview_USA.NDX_components import NDX_components_get_stock_data

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        NDX_components_get_stock_data()
        self.stdout.write(self.style.SUCCESS('Данные NDX_Components успешно сохранены в базу данных.'))