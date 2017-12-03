from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1
	random_string = get_random_string(length=14)
	content = {"string":random_string}
	# Not sure why we were asked to do a form on this.
	# Nothing to post so just log a post vs get
	if request.method == 'GET':
		response = "I am index! and I am a get"
	elif request.method == 'POST':
		response = "I am index! and I am a post"
	return render(request,'index.html', content)

def reset(request):
	print 'In reset!!!!!'
	if 'attempt' in request.session:
		request.session['attempt'] = 0
	return redirect("/random_word")