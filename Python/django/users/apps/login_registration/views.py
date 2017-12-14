# app login_registration views.py
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# bcrypt needed for passwords
import bcrypt
from models import User
# This will handle /
def clear_sessions(request):
	if 'name' in request.session:
		del request.session['name']
	if 'registered' in request.session:
		del request.session['registered']
	if 'logged_in' in request.session:
		del request.session['logged_in']
	if 'first_name' in request.session:
		del request.session['first_name']
	if 'last_name' in request.session:
		del request.session['last_name']
	if 'email' in request.session:
		del request.session['email']
	if 'birthday' in request.session:
		del request.session['birthday']

def index(request):
	#Need to clean up the session variables.
	#Because this is not fully functional we
	#need to do  something here.
	if 'registered' in request.session or 'logged_in' in request.session:
		print "clearing sessions"
		clear_sessions(request)
	return render(request,'login_registration/index.html')

def register(request):
	if request.method == "POST":
		errors = User.objects.registration_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags="registration_error")
			#Set some session variables so we can repopulate the form.
			#I always hate it when I make a mistake on the form and it
			#is not repopulated.
			request.session['first_name'] = request.POST['first_name']
			request.session['last_name'] = request.POST['last_name']
			request.session['email'] = request.POST['email']
			request.session['birthday'] = request.POST['birthday']
			return redirect(reverse('index'))
		else:
			#Add session variable registered and name. Used in success
			request.session['name'] = request.POST['first_name']
			request.session['registered'] = True
			user = User.objects.create(first_name=request.POST['first_name'],
									   last_name=request.POST['last_name'],
									   email=request.POST['email'],
									   birthday=request.POST['birthday'],
									   password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
			return redirect(reverse('success'))
	else:
		print "register ---", request.method, "received. Expecting POST."
	return render(request,'login_registration/index.html')

def login(request):
	if request.method == "POST":
		errors = User.objects.login_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags="login_error")
		else:
			try:
				user = User.objects.get(email=request.POST['email'])
				request.session['name'] = user.first_name
				request.session['logged_in'] = True
				return redirect(reverse('success'))
			except Exception as e:
				print 'login --- %s (%s)' % (e.message, type(e))
	return redirect(reverse('index'))

def success(request):
	return render(request,'login_registration/success.html')