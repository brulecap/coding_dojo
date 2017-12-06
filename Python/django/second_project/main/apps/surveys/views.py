# app surveys views.py
from django.shortcuts import render, HttpResponse, redirect
# function is called when /surveys is visited
def index(request):
	return HttpResponse("placeholder to display all the surveys created")

# function is called when /surveys/new is visited
def new(request):
	return HttpResponse("placeholder for users to add a new survey")