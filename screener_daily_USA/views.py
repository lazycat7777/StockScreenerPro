from django.shortcuts import render
from .models import StockData
import json

def index_html(request):
    return render(request, 'index.html')

def screener_html(request):
    stock_data = StockData.objects.all().values()
    data = list(stock_data) 
    return render(request, 'screener.html', {'data': json.dumps(data)}) 

