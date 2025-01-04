import time
from datetime import timedelta
from screener_website.celery_app import app
from .service import cleanup_expired_access

# Удаляем устаревшие записи IP адресов
@app.task
def remove_expired_ip_access():
    start_time = time.time()  

    cleanup_expired_access()

    end_time = time.time()  
    elapsed_time = end_time - start_time  
    elapsed_time_formatted = str(timedelta(seconds=elapsed_time))
    print(f'Селери таска завершена, устаревшие записи IP адресов удалены. Время выполнения: {elapsed_time_formatted}')