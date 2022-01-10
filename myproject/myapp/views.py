from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'Name': 'Arav',
        'Age': 35,
        'Nationality': 'American'
    }
    return render(request, 'index.html', context)

def counter(request):
    x = request.GET['pack']
    y = len(x.split())
    return render(request, 'counter.html', {'y': y, 'x': x} )