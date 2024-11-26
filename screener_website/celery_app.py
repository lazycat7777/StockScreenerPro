import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'screener_website.settings')

app = Celery('screener_website')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'calculate_results_USA': {
        'task': 'screener_daily_USA.tasks.calculate_results_USA',
        'schedule': crontab(minute=0, hour=3),
    },
    'cleanup_expired_ip_access': {
        'task': 'auth_telegram_bot.tasks.remove_expired_ip_access',
        'schedule': crontab(minute=0, hour=0),
    }
}
