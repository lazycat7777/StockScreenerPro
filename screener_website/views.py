from django.shortcuts import render

def index_html(request):
    return render(request, 'index.html')
