# app users views.py
from django.shortcuts import render, HttpResponse, redirect
# function is called when /users is visited
def index(request):
	return HttpResponse("placeholder to later display all the list of users")

# function is called when /register or /users/new is visited
def register(request):
	return HttpResponse("placeholder for users to create a new user record")

# function is called when /login is visited
def login(request):
	return HttpResponse("placeholder for users to login")