from screener_daily_USA.update_stock_data_USA.calculate_results_main import calculate_and_aggregate_results

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        calculate_and_aggregate_results()
        self.stdout.write(self.style.SUCCESS('Данные Stock_Data_Indicators успешно обновлены'))