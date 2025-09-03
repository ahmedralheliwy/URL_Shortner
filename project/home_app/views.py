from django.shortcuts import render,redirect
from .models import URL_Box
from .forms import URL_Form
import requests

def home(request):
    if request.method == 'POST':
        form=URL_Form(request.POST)
        if  form.is_valid():
            obj=form.save()
            url=obj.URL
            short_url=shorten_url(url)
            context={'short_url':short_url}
            return render(request,'shorten_url.html',context)
    else:
        form=URL_Form()
    context={"form":form}
    return render(request,'home.html',context)
    
def shorten_url(long_url):
    url='https://api-ssl.bitly.com/v4/shorten'
    headers={'Authorization':'Bearer 336edd6d73598a9aa58594c63a953a37a5a5b22f'} 
    json_data={'long_url':long_url}
    response=requests.post(url,headers=headers,json=json_data)
    print('---------------------------')
    print('---------------------------')
    print('---------------------------')
    print(f'status code {response.status_code}')
    print('---------------------------')
    print('---------------------------')
    print('---------------------------')
    if response.status_code==200:
        return response.json()['link']
    else:
        return "Error in shorten url"
    