from django.urls import path
from . import views

app_name = 'screener_daily_USA'

urlpatterns = [
    path('screener/', views.screener_html, name='screener'),
    path('stock_heatmap_SPX/', views.stock_heatmap_SPX_html, name='stock_heatmap_SPX'),
    path('stock_heatmap_NDX/', views.stock_heatmap_NDX_html, name='stock_heatmap_NDX'),
]


