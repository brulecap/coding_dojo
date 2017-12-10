# app book_authors models.py
from __future__ import unicode_literals
from django.db import models
class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(default='Description needed!')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {}>".format(self.name)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	notes = models.TextField(default='Note needed!')
	books = models.ManyToManyField(Book, related_name="authors")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {} {}>".format(self.first_name, self.last_name)