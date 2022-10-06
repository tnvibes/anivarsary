import http
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """return HttpResponse("This is homePage")"""
    return render(request, 'index.html')
def crypto(request):
    #return HttpResponse("ths is login page")
    return render(request, 'index.html')

def signup(request):
    return HttpResponse("this is signup page")

def writer(request):
    return HttpResponse("this is writer page")

def coder(request):
    return HttpResponse("this is coder page")

def insta(request):
    #return HttpResponse("ths is login page")
    return render(request, 'insta.html')

