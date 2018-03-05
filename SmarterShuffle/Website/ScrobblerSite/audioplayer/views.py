from django.shortcuts import render,render_to_response
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import hashlib

API_KEY="e994e38da0dffa0d754afaadab0b8c90"
Secret="06cbc89c47c9580ceea04493b735b432"

# Create your views here.
def index(request):
    return render(request, 'audioplayer/index.html')

def play(request):
    url = "https://www.youtube.com/watch?v=8367ETnagHo"
    signin_url='http://www.last.fm/api/auth/?api_key=%s' %API_KEY
    return HttpResponseRedirect(signin_url)

def login_complete(request):
    token = request.GET["token"]

    #session="api_key%smethodauth.getSessiontoken%s" %(API_KEY.encode('utf-8'),token.encode('utf-8'))
    
    #api_signa=hashlib.md5(session.encode()).hexdigest()

    #url="http://ws.audioscrobbler.com/2.0/?method=auth.getSession&api_key=%s &token=%s &api_sig=%s" %(API_KEY,token,api_signa)

    #return HttpResponseRedirect(url)

    #ses=requests.get(url)

    #request.session['username']=ses['name']
    
    user = authenticate(token=token)
    if user:
        login(request, user)

    return HttpResponseRedirect("/admin/")
    
