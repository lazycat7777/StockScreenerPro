import os
from celery import Celery
from django.conf import settings
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'screener_website.settings')

app = Celery('screener_website')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

@app.task()
def debug_task():
    time.sleep(10)
    print('Тестовый таск отработал')



