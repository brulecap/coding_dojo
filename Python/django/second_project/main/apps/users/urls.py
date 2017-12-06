#app users urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^register/$', views.register), #/register
	url(r'^new/$', views.register), #/users/new
	url(r'^login/$', views.login), #/login
	url(r'^$', views.index) #/users
]