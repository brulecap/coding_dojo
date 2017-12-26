# app reviews views.py
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# bcrypt needed for passwords
import bcrypt
# import db models
from models import *
# constant used in rendering templates in this view
APP_NAME = 'reviews'
MAX_RECENT_REVIEWS = 5

def clear_register_session(request):
	if 'name' in request.session:
		del request.session['name']
	if 'alias' in request.session:
		del request.session['alias']
	if 'email' in request.session:
		del request.session['email']
	if 'register' in request.session:
		del request.session['register']
	if 'login' in request.session:
		del request.session['login']		

def not_logged_in(func):
	def decorated(request, *args, **kwargs):
		if 'logged_in' in request.session and request.session['logged_in']:
			return redirect(reverse('books'))
		return func(request, *args, **kwargs)
	return decorated

def log_in_required(func):
	def decorated(request, *args, **kwargs):
		if 'logged_in' not in request.session or not request.session['logged_in']:
			return redirect(reverse('index'))
		return func(request, *args, **kwargs)
	return decorated

def index(request):
	return render(request, APP_NAME + '/index.html')

# This view handles the signin/ url and the post from the signin/ url.
@not_logged_in
def signin(request):
	if 'register' in request.session:
		del request.session['register']

	if request.method == "POST":
		if User.objects.login_validator(request):
			content = User.objects.get_user_dict(request, {"email":request.POST['email']})
			if content:
				clear_register_session(request)
				request.session['logged_in'] = True
				request.session['id'] = content['id']
				request.session['name'] = content['name']
				return redirect(reverse('books'))
		else:
			request.session['login'] = True
	return redirect(reverse('index'))

# This view handles the register/ url. 
@not_logged_in
def register(request):
	if request.method == "POST":
		if not User.objects.user_validator(request):
			if 'login' in request.session:
				del request.session['login']
			# Set some session variables so we can repopulate the form.
			# I always hate it when I make a mistake on the form and it
			# is not repopulated.
			request.session['register'] = True
			request.session['name'] = request.POST['name']
			request.session['alias'] = request.POST['alias']
			request.session['email'] = request.POST['email']
			return redirect(reverse('index'))
		else:
			try:
				user = User.objects.create(name=request.POST['name'],
										   alias=request.POST['alias'],
										   email=request.POST['email'],
										   password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
				# Add session variable registered. Used in the login page.
				request.session['registered'] = True
				messages.success(request, 'Congratulations ' + request.POST['name'] + '! You have successfully registered. Please login below.')
				clear_register_session(request)
				return redirect(reverse('index'))
			except Exception as e:
				print 'register --- %s (%s)' % (e.message, type(e))
				messages.error(request, 'Not quite sure what happened there. Please try to register again. If the problem persists contact the site help desk.')
				return redirect(reverse('index'))	
	return redirect(reverse('index'))

# This view handles the signout/ url.
@log_in_required
def signout(request):
	#For now we will flush all session variables. I can't think of a reason we would need any ATT.
	request.session.flush()
	return redirect(reverse('index'))

@log_in_required
def books(request, id=''):
	if id == "":
		reviews = Review.objects.all().order_by("-created_at")
		return render(request, APP_NAME + '/books.html', {'reviews':reviews})
	else:
		try:
			book = Book.objects.get(id=id)
			return render(request, APP_NAME + '/book.html', {'book':book})
		except:
			messages.error(request, 'There was a problem with that request. If the problem persists contact the site help desk.')
			redirect(reverse('books'))

@log_in_required
def add(request):
	if request.method == "GET":
		authors = Author.objects.all()
		return render(request, APP_NAME + '/add.html', {'authors':authors})
	elif request.method == "POST":
		print request.POST
		if Review.objects.validate_review(request):
			Review.objects.add_review(request)
		else:
			return render(request, APP_NAME + '/add.html')
	return redirect(reverse('books'))

@log_in_required
def user(request, id):
	print 'in user', id
	try:
		print 'in try'
		user = User.objects.get(id=id)
		return render(request, APP_NAME + '/user.html', {'user':user})
	except Exception as e:
		print 'excpetion'
		print 'register --- %s (%s)' % (e.message, type(e))
		messages.error(request, 'There was a problem with that request. Please try again. If the problem persists contact the site help desk.')
	return redirect(reverse('books'))