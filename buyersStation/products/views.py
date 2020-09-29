from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def index(request):
    return HttpResponse('products page')


def details(request, pk):
    return HttpResponse('first product detail')