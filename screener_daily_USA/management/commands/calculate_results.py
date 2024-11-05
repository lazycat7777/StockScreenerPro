from screener_daily_USA.update_stock_data.calculate_results_main import calculate_and_aggregate_results

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Обновляет данные о акциях и рассчитывает индикаторы'

    def handle(self, *args, **options):
        calculate_and_aggregate_results()
        self.stdout.write(self.style.SUCCESS('Данные успешно обновлены'))