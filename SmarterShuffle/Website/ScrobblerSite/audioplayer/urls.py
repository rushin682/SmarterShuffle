from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'^index$', views.index, name='index'),
               url(r'^play$',views.play,name='play'),
               url('^login_complete/$', views.login_complete, name='lastfm_login_complete'),
               url(r'^logout$',views.logout,name='logout'),
               url(r'^search_query', views.youtubeurl, name = 'youTube_query'),
               url(r'^search_query/(?P<video_id>\w+)/', views.pafy, name = 'pafy') 
               ]
