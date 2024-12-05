from django.core.management.base import BaseCommand
from screener_daily_USA.update_stock_data_USA.merge_all_tables import merge_tables, save_merge_tables_to_db

class Command(BaseCommand):

    def handle(self, *args, **options):
        merged_data = merge_tables()
        save_merge_tables_to_db(merged_data)
        self.stdout.write(self.style.SUCCESS('Данные Stock_Merge_All_Tables сохранены.'))
