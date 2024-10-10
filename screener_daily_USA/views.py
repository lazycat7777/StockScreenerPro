from django.shortcuts import render
from .models import StockData
from django.db.models import F
# from .forms import FilterForm


def index_html(request):
    return render(request, 'index.html')

def screener_html(request):
    data = StockData.objects.using('default').all()
    Quick_filter_selected_filter = request.GET.get('Quick filter')
    Exchange_NYSE_selected_filter = request.GET.get('Exchange_NYSE')
    Exchange_NASDAQ_selected_filter = request.GET.get('Exchange_NASDAQ')
    SMA_10_selected_filter = request.GET.get('10-Day SMA')

    # Quick filter
    if Quick_filter_selected_filter == 'Quick filter 1':
        data = StockData.objects.filter(
            ADR_percent__gt=3.5,
            SMA_10__gt=F('SMA_20'), 
            SMA_20__gt=F('SMA_50'), 
            SMA_50__gt=F('SMA_100'),
            SMA_100__gt=F('SMA_200')
            )

    if Quick_filter_selected_filter == 'Quick filter 2':
        data = StockData.objects.filter(
            ADR_percent__gt=3.5,
            SMA_20__gt=F('SMA_50'), 
            SMA_50__gt=F('SMA_100'),
            SMA_100__gt=F('SMA_200')
            )

    if Quick_filter_selected_filter == 'Quick filter 3':
        data = StockData.objects.filter(
            ADR_percent__gt=3.5,
            SMA_50__gt=F('SMA_100'),
            SMA_100__gt=F('SMA_200')
            )


    # Exchanges
    elif Exchange_NYSE_selected_filter == 'NYSE' and Exchange_NASDAQ_selected_filter == 'NASDAQ':
        data = StockData.objects.filter(
            exchange__in=['NYSE', 'NASDAQ']
            )

    elif Exchange_NYSE_selected_filter == 'NYSE':
        data = StockData.objects.filter(
            exchange='NYSE'
            )

    elif Exchange_NASDAQ_selected_filter == 'NASDAQ':
        data = StockData.objects.filter(
            exchange='NASDAQ'
            )




    # SMA_10
    elif SMA_10_selected_filter == 'SMA10 above SMA20':
        data = StockData.objects.filter(SMA_10__gt=F('SMA_20')) 
    
    elif SMA_10_selected_filter == 'SMA10 above SMA50':
        data = StockData.objects.filter(SMA_10__gt=F('SMA_50'))  

    elif SMA_10_selected_filter == 'SMA10 above SMA100':
        data = StockData.objects.filter(SMA_10__gt=F('SMA_100'))  

    elif SMA_10_selected_filter == 'SMA10 above SMA150':
        data = StockData.objects.filter(SMA_10__gt=F('SMA_150'))  

    elif SMA_10_selected_filter == 'SMA10 above SMA200':
        data = StockData.objects.filter(SMA_10__gt=F('SMA_200'))  

    elif SMA_10_selected_filter == 'SMA10 below SMA20':
        data = StockData.objects.filter(SMA_10__lt=F('SMA_20'))                  

    elif SMA_10_selected_filter == 'SMA10 below SMA50':
        data = StockData.objects.filter(SMA_10__lt=F('SMA_50'))  

    elif SMA_10_selected_filter == 'SMA10 below SMA100':
        data = StockData.objects.filter(SMA_10__lt=F('SMA_100'))  

    elif SMA_10_selected_filter == 'SMA10 below SMA150':
        data = StockData.objects.filter(SMA_10__lt=F('SMA_150'))  

    elif SMA_10_selected_filter == 'SMA10 below SMA200':
        data = StockData.objects.filter(SMA_10__lt=F('SMA_200'))  













    # data = StockData.objects.filter(SMA_10__gt=F('SMA_20'))
    return render(request, 'screener.html', {'data': data})



# a = StockData.objects.filter(SMA_10__gt=F('SMA_20'))


# def screener_html(request):
#     data = StockData.objects.using('screener_daily_USA_db').all()
#     SMA10_dropdown = request.GET.get('10-Day SMA')
#     print(SMA10_dropdown)

#     if SMA10_dropdown == 'SMA10_above_SMA20':
#         data = data.filter(SMA_10__gtSMA_20)  # Фильтруем по SMA10 > SMA20
# #     elif condition == 'SMA10_below_SMA50':
# #         data = data.filter(SMA10__lt=SMA50)  # Фильтруем по SMA10 < SMA50
# #     # ... и так далее для других условий

#     return render(request, 'screener.html', {'data': data})


# def screener_html(request):
#     condition = request.GET.get('condition')
#     data = StockData.objects.using('screener_daily_USA_db').all()

#     if condition:
#         if condition == 'SMA10_above_SMA20':
#             data = data.filter(SMA_10__gt=StockData.SMA_20)
#         # ... и так далее для других условий

#     return render(request, 'screener.html', {'data': data})

# def screener_html(request):
#     data = StockData.objects.using('screener_daily_USA_db').all()
#     return render(request, 'screener.html', {'data': data})