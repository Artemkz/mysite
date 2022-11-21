from django.shortcuts import render
from .models import Products


def stock_home(request):
    product = Products.objects.all()
    return render(request, 'stock/stock_home.html', {'product':product})