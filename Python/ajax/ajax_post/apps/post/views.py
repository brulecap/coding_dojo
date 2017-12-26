# app post views.py
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import *

# constant used in rendering templates in this view
APP_NAME = 'post'
def index(request):
	return render(request, APP_NAME + '/index.html')

def all_json(request):
	print 'all json'
	return render(request, APP_NAME + '/index.html')

def all_html(request):
	print request.POST
	if request.method == "POST" and request.POST['note']:
		Note.objects.create(note=request.POST['note'])
		notes = Note.objects.all()
		return render(request, APP_NAME + '/post.html', {'notes':notes})
	else:
		return render(request, APP_NAME + '/post.html')