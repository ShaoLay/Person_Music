from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def userView(request):
    return HttpResponse('这是个人')
