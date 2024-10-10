from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_html, name='index'),
    path('screener/', views.screener_html, name='screener'),
]


