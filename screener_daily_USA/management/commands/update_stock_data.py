from django.core.management.base import BaseCommand
from screener_daily_USA.screener_daily_USA_main import calculate_and_aggregate_results

class Command(BaseCommand):
    help = 'Обновляет данные о акциях и рассчитывает индикаторы'

    def handle(self, *args, **options):
        calculate_and_aggregate_results()
        self.stdout.write(self.style.SUCCESS('Данные успешно обновлены'))
        # self.stdout.write(self.style.SUCCESS(print(calculate_and_aggregate_results())))