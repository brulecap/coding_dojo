from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^new/$', views.new, name="users_new"),
	url(r'^users/create/$', views.create, name="users_create"),
	url(r'^users/update/$', views.update, name="users_update"),
	url(r'^users/(?P<id>\w+)/edit/$', views.edit, name="users_edit"),
	url(r'^users/(?P<id>\w+)/destroy/$', views.destroy, name="users_destroy"),
	url(r'^users/(?P<id>\w+)$', views.show, name="users_show"),
	url(r'^', views.index, name="users_index")
]