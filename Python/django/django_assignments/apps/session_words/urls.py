from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^clear/$', views.clear),
	url(r'^process/$', views.process),
	url(r'^', views.index)
]