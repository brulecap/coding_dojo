from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request, content=''):
	print 'in index'
	return render(request,'index.html')

def process(request):
	print 'in process'
	error = False
	text_size = 'regular'
	if request.method == 'POST':
		if 'word' not in request.POST or len(request.POST['word']) < 1:
			error = True
			messages.error(request, 'Please enter a word.')
		if 'color' not in request.POST:
			error = True
			messages.error(request, 'Please select a color.')
		if 'big' in request.POST:
			text_size = 'big'
		if not error:
			if 'word_list' not in request.session:
				print 'new session'
				request.session['word_list'] = []
			print request.session['word_list']
			word_format = {"word":request.POST['word'],
						   "color":request.POST['color'],
						   "text_size":text_size}
			request.session['word_list'].append(word_format)
			request.session.modified = True
			print request.session['word_list']
	#Redirect to session_word page regardless of any errors.
	return redirect("/session_words")

def clear(request):
	print 'In clear'
	if 'word_list'  in request.session:
		del request.session['word_list']
		request.session.modified = True
	return redirect("/session_words")