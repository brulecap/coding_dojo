#time_display URL Configuration
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
	url(r'^', include('apps.display.urls'))
]