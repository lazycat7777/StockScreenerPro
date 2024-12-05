from auth_telegram_bot.utils import ip_access_required
from django.shortcuts import render
from .models import Stock_Merge_All_Tables
import json

@ip_access_required
def screener_html(request):
    stock_data = Stock_Merge_All_Tables.objects.all().values()
    data = list(stock_data) 
    return render(request, 'screener.html', {'data': json.dumps(data)}) 

@ip_access_required
def stock_heatmap_SPX_html(request):
    return render(request, 'stock_heatmap_SPX.html')

@ip_access_required
def stock_heatmap_NDX_html(request):
    return render(request, 'stock_heatmap_NDX.html')