from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connections['tradingview_data_db'].cursor() as cursor:
            cursor.execute("SELECT symbol FROM stock_data_overview")
            rows = cursor.fetchall()
            
            symbols_and_exchanges = []
            for row in rows:
                full_symbol = row[0]
                if ':' in full_symbol:
                    exchange, symbol = full_symbol.split(':')
                    symbols_and_exchanges.append((symbol, exchange))

        # Вывод результата
        self.stdout.write(str(symbols_and_exchanges))
