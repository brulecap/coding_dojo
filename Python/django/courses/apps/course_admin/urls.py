#app course_admin urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^new/$', views.new, name="course_admin_new"),
	url(r'^destroy/(?P<id>\w+)/$', views.destroy, name="course_admin_destroy"),
	url(r'^destroy/$', views.destroy, name="course_admin_destroy"),
	url(r'^', views.index, name="course_admin_index")
]