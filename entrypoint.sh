#!/bin/bash
source /ctr-py-venv/bin/activate
# python manage.py makemigrations
# python manage.py migrate 
# python manage.py migrate --fake-initial
# python manage.py migrate --run-syncdb
# python manage.py makemigrations screener_daily_USA
# python manage.py migrate --fake
# python manage.py calculate_results
# python manage.py symbols_and_exchanges
# python manage.py save_data_dividends
python manage.py runserver 0.0.0.0:18080





