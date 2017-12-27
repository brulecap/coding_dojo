# app post urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^delete/$', views.delete, name="delete"),
	url(r'^update/$', views.update, name="update"),
	url(r'^create/$', views.create, name="create"),
	url(r'^init/$', views.init, name="init"),
	url(r'^', views.index, name="index")
]