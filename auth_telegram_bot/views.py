from django.shortcuts import render
from .service import get_client_ip, is_ip_in_database, add_ip_to_database

# Переход в регистрацию через телеграм бота
def Telegram_Login_View(request):
    return render(request, 'to_telegram_bot.html')

# Добавление IP в базу данных
def grant_access(request):
    client_ip = get_client_ip(request)

    if not is_ip_in_database(client_ip):
        add_ip_to_database(client_ip)
    
    if is_ip_in_database(client_ip):
        message = "Success! You are logged in!"
    else:
        message = "Long response from server. Refresh this page!"

    return render(request, 'telegram_bot_access.html', {'message': message})
