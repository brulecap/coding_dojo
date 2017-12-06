# app blogs views.py
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root or blogs is visited
def index(request):
	print "in blogs index"
	return HttpResponse("placeholder to later display all the list of blogs")

# the new function is called when blogs/new is visited
def new(request):
	print "in blogs new"
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

# the create function is called when blogs/create is visited
def create(request):
	print "in blogs create"
	return redirect("/blogs")

# the show function is called when blogs/{{number}} is visited
def show(request, number):
	print "in blogs show"
	return HttpResponse("placeholder to display blog " + str(number))

# the edit function is called when blogs/{{number}}/edit is visited
def edit(request, number):
	print "in blogs edit"
	return HttpResponse("Placeholder to edit blog " + str(number))

# the edit function is called when blogs/{{number}}/delete is visited
def destroy(request, number):
	print "Destroying " + str(number)
	return redirect('/blogs')