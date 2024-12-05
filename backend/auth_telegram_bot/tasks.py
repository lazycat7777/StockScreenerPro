from celery import shared_task
from .service import cleanup_expired_access

# Удаляем устаревшие записи IP адресов
@shared_task
def remove_expired_ip_access():
    cleanup_expired_access()
