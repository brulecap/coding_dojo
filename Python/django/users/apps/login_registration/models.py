# app login_registration models.py
from __future__ import unicode_literals
from django.db import models
# re used to validate emails
import re
# datetime and relativedelta used to validate birthday
from datetime import datetime
from dateutil.relativedelta import relativedelta
# bcrypt needed for passwords
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def registration_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 2:
			errors["first_name"] = "First name should be more than 1 character."
		if len(postData['last_name']) < 2:
			errors["last_name"] = "Last name should be more than 1 character."
		if not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Invalid email address."
		elif User.objects.filter(email=postData['email']).count() > 0:
			errors["email"] = "That email is already associated with an account"
		try:
			if datetime.strptime(postData['birthday'], "%Y-%m-%d") > datetime.now() - relativedelta(years=10):
				errors["birthday"] = 'You are too young. Please have you parents register.'
		except:
			errors["birthday"] = "There was a problem with the birthday entered."
		if len(postData['password']) < 8:
			errors["password"] = "The password must be at least 8 characters."
		elif postData['password'] != postData['confirm']:
			errors["password"] = "The password and confirmation password must match."
		return errors
	def login_validator(self, postData):
		errors = {}
		if not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Invalid email address."
		else:
			email_count = User.objects.filter(email=postData['email']).count()
			if email_count < 1:
				errors["email"] = "That email not associated with an account"
			elif email_count > 1:
				#This should not happen.
				errors["email"] = "Server error. Please contact customer support for help"
				print "login_validator --- Email address", postData['email'], "associated with more than 1 account."
		if len(postData['password']) < 8:
			errors["password"] = "The password must be at least 8 characters."
		try:
			user = User.objects.get(email=postData['email'])
			if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				errors["password"] = "That email/password combination did not work."
		except Exception as e:
			print 'login_validator --- %s (%s)' % (e.message, type(e))
			errors["password"] = "Server error. Please contact customer support for help"

		return errors
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return "<User object: {} {}>".format(self.first_name, self.last_name)