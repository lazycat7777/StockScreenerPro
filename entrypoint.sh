#!/bin/bash
source /venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:18080











# source /venv/bin/activate
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 0.0.0.0:18080