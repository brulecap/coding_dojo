from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	url(r'^(\d+)/edit$', views.edit),
	url(r'^(\d+)/delete$', views.destroy),
	url(r'^(\d+)$', views.show),
	url(r'^$', views.index)
]