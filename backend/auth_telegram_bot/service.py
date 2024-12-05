from django.utils.timezone import now
from datetime import timedelta
from .models import IPAccess

# Извлечение IP-адреса клиента
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')

# Проверка наличия IP-адреса в базе
def is_ip_in_database(ip_address):
    return IPAccess.objects.filter(ip_address=ip_address).exists()

# Добавление нового IP-адреса
def add_ip_to_database(ip_address):
    expiration_date = now().date() + timedelta(days=30)
    IPAccess.objects.create(ip_address=ip_address, expiration_date=expiration_date)

# Удаление устаревших записей
def cleanup_expired_access():
    IPAccess.objects.filter(expiration_date__lte=now().date()).delete()
