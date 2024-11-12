from django.shortcuts import render
from .models import Stock_Merge_All_Tables
import json

def index_html(request):
    return render(request, 'index.html')

def screener_html(request):
    stock_data = Stock_Merge_All_Tables.objects.all().values()
    data = list(stock_data) 
    return render(request, 'screener.html', {'data': json.dumps(data)}) 

