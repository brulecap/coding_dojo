# app post urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
#	url(r'^register/$', views.register, name="register"),
#	url(r'^users/(?P<id>\w+)/$', views.user, name="user"),
#	url(r'^signout/$', views.signout, name="signout"),
#	url(r'^signin/$', views.signin, name="signin"),
#	url(r'^books/add/$', views.add, name="add"),
#	url(r'^books/(?P<id>\w+)/$', views.books, name="books"),
#	url(r'^books/$', views.books, name="books"),
	url(r'^all.html$', views.all_html, name="all_html"),
	url(r'^all.json$', views.all_json, name="all_json"),
	url(r'^', views.index, name="index")
]