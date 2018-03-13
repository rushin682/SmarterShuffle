from django.shortcuts import render,render_to_response
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import hashlib
import json
import xml.etree.ElementTree as ET



API_KEY="e994e38da0dffa0d754afaadab0b8c90"
Secret="06cbc89c47c9580ceea04493b735b432"
ytkey="AIzaSyAeBQCitMcOktbV4jPZqoF10Lve62I-jr8"

# Create your views here.
def index(request):
    return render(request, 'audioplayer/index.html')

def play(request):
    url = "https://itunes.apple.com/search?term=havana&country=IN&media=music&entity=musicTrack&attribute=songTerm"
    signin_url='http://www.last.fm/api/auth/?api_key=%s' %API_KEY
    #music=requests.get(url)
    #print(music[0)
    return HttpResponseRedirect(signin_url)

def login_complete(request):
    token = request.GET["token"]

    sig_param="api_key%smethodauth.getSessiontoken%s%s" %(API_KEY,token,Secret)
    
    api_signa=hashlib.md5(sig_param.encode()).hexdigest()

    print(api_signa)
    

    url="http://ws.audioscrobbler.com/2.0/?method=auth.getSession&token=%s&api_key=%s&api_sig=%s" %(token,API_KEY,api_signa)

    #return HttpResponseRedirect(url)

    ses=requests.get(url)
    ses=ses.content.decode()
    #ses=json.loads(ses)
    #ses=json.dumps(ses)
    root = ET.fromstring(ses)
    print(root[0][0].text);

    
    request.session['username']=root[0][0].text
    print("here")
    
    #request.session['username']=ses['name']
    
    user = authenticate(token=token)
    if user:
        login(request, user)

    return HttpResponseRedirect("/ap/index")
    
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass

    return HttpResponseRedirect("/ap/index")

def youtubeurl(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', None)
    
    url1="https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=3&q=%s&type=video&key=%s" %(search_query,ytkey)
    videodetails=requests.get(url1)
    videodetails = videodetails.json()
   # for item_num in videodetails :
       # dictionary[item_num] = item_num['snippet']
    return render(request, 'audioplayer/index.html', {'videodetails':videodetails})
    #songurl="https://www.youtube.com/watch?v=%s" %(videoid) '''

    
    
