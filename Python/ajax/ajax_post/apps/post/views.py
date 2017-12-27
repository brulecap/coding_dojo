# app post views.py
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import *
from django.core import serializers
import json

# constant used in rendering templates in this view
APP_NAME = 'post'
def index(request):
	return render(request, APP_NAME + '/index.html')

def init(request):
	print 'in init'
	return render(request, APP_NAME + '/post.html', {'notes':Note.objects.all()})

def create(request):
	if request.method == "POST" and request.POST['title']:
		Note.objects.create(title=request.POST['title'])
	return render(request, APP_NAME + '/post.html', {'notes':Note.objects.all()})

def update(request):
	if request.method == "POST" and request.POST['note']:
		note = Note.objects.get(id=request.POST['id'])
		note.note = request.POST['note']
		note.save()
	return render(request, APP_NAME + '/post.html', {'notes':Note.objects.all()})

def delete(request):
	if request.method == "POST" and request.POST['id']:
		Note.objects.get(id=request.POST['id']).delete()
	return render(request, APP_NAME + '/post.html', {'notes':Note.objects.all()})