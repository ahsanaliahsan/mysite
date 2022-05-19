from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. I am changed now.")

def index2(request):
    return HttpResponse("So I am index2 ? ")

def index3(request):
    return HttpResponse("INDEX 3")