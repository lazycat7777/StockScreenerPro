from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_html, name='index'),
    path('screener/', views.screener_html, name='screener'),
    path('stock_heatmap_SPX/', views.stock_heatmap_SPX_html, name='stock_heatmap_SPX'),
    path('stock_heatmap_NDX/', views.stock_heatmap_NDX_html, name='stock_heatmap_NDX'),
]


