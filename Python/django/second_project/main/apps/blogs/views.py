from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "This is index!"
	return HttpResponse(response)
# the new function is called when /new is visited
def new(request):
	response = "This is new!"
	return HttpResponse(response)
# the create function is called when /create is visited
def create(request):
	print 'Creating'
	return redirect('/')
# the show function is called when /{{number}} is visited
def show(request, number):
	response = "Placeholder to display blog " + str(number)
	return HttpResponse(response)
# the edit function is called when /{{number}}/edit is visited
def edit(request, number):
	response = "Placeholder to edit blog " + str(number)
	return HttpResponse(response)
# the edit function is called when /{{number}}/delete is visited
def destroy(request, number):
	print "Destroying " + str(number)
	return redirect('/')