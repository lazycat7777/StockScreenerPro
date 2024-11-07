# merge_stock_data.py
from django.core.management.base import BaseCommand
from screener_daily_USA.update_stock_data_USA.merge_all_tables import merge_tables

class Command(BaseCommand):

    def handle(self, *args, **options):
        merge_tables()
        self.stdout.write(self.style.SUCCESS('Данные merge_tables сохранены.'))
