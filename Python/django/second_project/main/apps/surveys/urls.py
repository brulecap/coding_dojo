#app surveys urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^new/$', views.new), #/surveys/new
	url(r'^$', views.index) #/surveys
]