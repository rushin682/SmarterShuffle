from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'^index$', views.index, name='index'),
               url(r'^play$',views.play,name='play'),
               url('^login_complete/$', views.login_complete, name='lastfm_login_complete'),
               url(r'^logout$',views.logout,name='logout'),
               #url(r'^(?P<videoid>\[a-zA-Z0-9])$',views.pafy1,name='pafy'),
               #url(r'',views.pafy1,name='pafy'),
               url(r'^search_query', views.youtubeurl, name = 'youTube_query'),]
