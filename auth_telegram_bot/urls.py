from django.urls import path
from . import views

urlpatterns = [
    path('to_telegram_bot/', views.to_telegram_bot_html, name='to_telegram_bot'),
    path('telegram_bot_access/', views.telegram_bot_access_html, name='telegram_bot_access'),
]
