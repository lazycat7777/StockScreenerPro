from django.shortcuts import render

def index_html(request):
    return render(request, 'index.html')

def contact_us_html(request):
    return render(request, 'contact_us.html')