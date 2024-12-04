from django.shortcuts import redirect
from .models import IPAccess

def ip_access_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        client_ip = get_client_ip(request)
        # Проверка IP-адреса
        if not IPAccess.objects.filter(ip_address=client_ip).exists():
            return redirect('to_telegram_bot') # перенаправление
        return view_func(request, *args, **kwargs)

    return _wrapped_view

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')
