from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse 
from .models import *


def index(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'products/index.html', context )


def details(request, product_id):
    #product = Product.objects.get(id= pk)
    # product = get_object_or_404(Product, pk=product_id)
    # context = {
    #     'product' : product
    # }
    return render(request, 'products/details.html', { 'product' : get_object_or_404(Product, pk=product_id)} )