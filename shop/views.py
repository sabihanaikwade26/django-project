from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('aboutUS page')

def contact(request):
    return HttpResponse('contactUs page')

def search(request):
    return HttpResponse('search page')

def productView(request):
    return HttpResponse('productView page')