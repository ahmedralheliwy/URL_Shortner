from django.shortcuts import render
from .models import URL_Box

def home(request):
    context={}
    return render(request,'home.html',context)
    
def shorten_url(request):
    context={}
    return render(request,'shorten_url.html',context)
    