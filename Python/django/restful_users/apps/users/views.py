from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User
# This will handle / and /users
def index(request):
	users = User.objects.all()
	return render(request,'users/index.html', {'users': users})

# This will handle /new/
def new(request):
	return render(request,'users/new.html')

# This will handle /users/<id>/
def show(request, id=''):
	try:
		user = User.objects.get(id=id)
		return render(request,'users/show.html', {'user': user})
	except Exception as e:
		#Should not get here. Print error and redirect home.
		print '%s (%s)' % (e.message, type(e))
		return redirect(reverse('users_index'))

# This will handle /users/<id>/edit/
def edit(request, id=''):
	try:
		user = User.objects.get(id=id)
		return render(request,'users/edit.html', {'user': user})
	except Exception as e:
		#Should not get here. Print error and redirect home.
		print '%s (%s)' % (e.message, type(e))
		return redirect(reverse('users_index'))

# This will handle POST from /users/new/
def create(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			form_fields = {'first':request.POST['first_name'], 'last':request.POST['last_name'], 'email':request.POST['email']}
			form_content = {"first_name":request.POST['first_name'],
							"last_name":request.POST['last_name'],
							"email":request.POST['email']}
			return render(request,'users/new.html', form_content)
		else:
			user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
			return redirect(reverse('users_show', kwargs={'id': user.id}))
	else:
		#Should never happen
		return redirect(reverse('users_index'))

# This will handle the POST from /users/<id>/edit/
def update(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			print request.POST['id']
			return redirect(reverse('users_edit', kwargs={'id': request.POST['id']}))
		else:
			user = User.objects.get(id=request.POST['id'])
			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.email = request.POST['email']
			user.save()
			return redirect(reverse('users_show', kwargs={'id': user.id}))
	else:
		#Should never happen
		return redirect(reverse('users_index'))

# This will handle /users/<id>/destroy/
def destroy(request, id=''):
	try:
		user = User.objects.get(id=id)
		user.delete()
	except Exception as e:
		#Should not get here. Print error and redirect home.
		print '%s (%s)' % (e.message, type(e))
		return redirect(reverse('users_index'))
	return redirect(reverse('users_index'))