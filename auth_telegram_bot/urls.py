from django.urls import path
from . import views

urlpatterns = [
    path('to_telegram_bot/', views.Telegram_Login_View, name='to_telegram_bot'),
    path('telegram_bot_access/', views.grant_access, name='telegram_bot_access'),
]
