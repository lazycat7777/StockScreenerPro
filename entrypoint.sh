#!/bin/bash
source /ctr-py-venv/bin/activate
# pip freeze
# pip install numpy==1.26.4 
# python manage.py makemigrations
# python manage.py migrate
# python manage.py update_stock_data
python manage.py runserver 0.0.0.0:18080
# python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'








