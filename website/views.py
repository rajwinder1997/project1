from django.shortcuts import render
from .forms import MyForm
import requests
import json
# Create your views here.
def index(request):
    f=MyForm()
    url="https://api.opencagedata.com/geocode/v1/json?q=PLACENAME&key=ca364b738f834866826765102f47917b"
    request=requests.GET(url)
    data=json.loads(request.text)
    return render(request,"index.html",{'f':f})
