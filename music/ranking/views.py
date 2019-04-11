from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def rankView(request):
    return HttpResponse('这是轮播')
