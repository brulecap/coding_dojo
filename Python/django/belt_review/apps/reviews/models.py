# app login_registration models.py
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
# re used to validate emails
import re
# bcrypt needed for passwords
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	# Validate registration fields
	def user_validator(self, request):
		errors = {}
		if len(request.POST['name']) < 2:
			errors["name"] = "Name should be more than 1 character."
		if len(request.POST['alias']) < 2:
			errors["alias"] = "Alias should be more than 1 character."
		if not EMAIL_REGEX.match(request.POST['email']):
			errors["emailr"] = "Invalid email address."
		elif User.objects.filter(email=request.POST['email']).count() > 0 and User.objects.get(email=request.POST['email']).id != id:
			errors["email"] = "That email is already associated with an account"
		if len(request.POST['password']) < 8:
			errors["password"] = "The password must be at least 8 characters."
		elif request.POST['password'] != request.POST['confirm']:
			errors["password"] = "The password and confirmation password must match."
		if len(errors):
			validated = False
			for tag, error in errors.iteritems():
				messages.error(request, error)
			return False
		return True

	# Validate login fields
	def login_validator(self, request):
		errors = {}
		if not EMAIL_REGEX.match(request.POST['email']):
			errors["email"] = "Invalid email address."
		else:
			email_count = User.objects.filter(email=request.POST['email']).count()
			if email_count < 1:
				errors["email"] = "That email not associated with an account"
			elif email_count > 1:
				#This should not happen.
				errors["email"] = "Server error. Please contact customer support for help"
				print "login_validator --- Email address", request.POST['email'], "associated with more than 1 account."
		if len(request.POST['password']) < 8:
			errors["password"] = "The password must be at least 8 characters."
		if len(errors) == 0:
			try:
				user = User.objects.get(email=request.POST['email'])
				if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
					errors["password"] = "That email/password combination did not work."
			except Exception as e:
				print 'login_validator --- %s (%s)' % (e.message, type(e))
				errors["password"] = "Server error. Please contact customer support for help"
		if len(errors) != 0:
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return False
		return True

	def get_user_dict(self, request, query_dict):
		content = {}
		try:
			user = User.objects.get(**query_dict)
			content = {'id':user.id,'name':user.name,'alias':user.alias,'email':user.email,'created_at':user.created_at,'updated_at':user.updated_at}
		except Exception as e:
			print 'get_user_dict --- %s (%s)' % (e.message, type(e))
			messages.error(request, 'There was an error retrieving user from the database. Please try again. If the problem persists, contact site help desk.')
		return content

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return "<User object: {}>".format(self.name)

class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {}>".format(self.title)

class Author(models.Model):
	name = models.CharField(max_length=255)
	book = models.ForeignKey(Book, null=True, related_name = "author")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {}>".format(self.name)

class ReviewManager(models.Manager):
	def validate_review(self, request):
		errors = {}
		if len(request.POST['title']) < 1:
			errors["title"] = "Title should have at least one 1 character."
		if len(request.POST['review']) < 8:
			errors["review"] = "A review should have at least 8 characters."
		if 'author' not in request.POST or len(request.POST['author']) == 0:
			#Author not selected from the list
			print request.POST
			if len(request.POST['new_author']) < 2:
				errors["new_author"] = "An author name should have at least 2 characters."
		if 'rating' not in request.POST or int(request.POST['rating']) < 1 or int(request.POST['rating']) > 5:
			errors["rating"] = "Please select a rating."
		if len(errors) != 0:
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return False
		return True

	def add_review(self,request):
		if (Book.objects.filter(title=request.POST['title']).count() > 0):
			book = Book.objects.get(title=request.POST['title'])
		else:
			book = Book.objects.create(title=request.POST['title'])
		if 'author' in request.POST and len(request.POST['author']) > 0:
			author = Author.objects.get(name=request.POST['author'])
		else:
			if (Author.objects.filter(name=request.POST['new_author']).count() > 0):
				author = Author.objects.get(name=request.POST['new_author'])
			else:
				author = Author.objects.create(name=request.POST['new_author'],book=book)
		user = User.objects.get(id=request.session['id'])
		review = Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],book=book,user=user)

class Review(models.Model):
	review = models.TextField()
	rating = models.PositiveSmallIntegerField()
	book = models.ForeignKey(Book, null=True, related_name = "review")
	user = models.ForeignKey(User, null=True, related_name = "review_creator")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ReviewManager()
	def __repr__(self):
		return "<User object: {}>".format(self.review)