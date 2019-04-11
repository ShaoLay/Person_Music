from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def searchView(request):
    return HttpResponse('这是搜索')
