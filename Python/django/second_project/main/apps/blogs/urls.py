#app blogs urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^new/$', views.new), #/blogs/new
	url(r'^create/$', views.create), #/blogs/create
	url(r'^(\d+)/edit/$', views.edit), #/blogs/{{number}}/edit
	url(r'^(\d+)/delete/$', views.destroy), #/blogs/{{number}}/delete
	url(r'^(\d+)$', views.show), #/blogs/{{number}}
	url(r'^', views.index) #/blogs and /
]