from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'^index$', views.index, name='index'),
               url(r'^play$',views.play,name='play'),
               url('^login_complete/$', views.login_complete, name='lastfm_login_complete')]
