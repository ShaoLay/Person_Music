from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def commentView(request):
    return HttpResponse('这是评论')
