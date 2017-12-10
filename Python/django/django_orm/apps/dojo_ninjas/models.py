# app dojo_ninjas models.py
from __future__ import unicode_literals
from django.db import models
class Dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField(default='Description needed!')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {} {} {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(Dojo, related_name="ninja")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {} {}>".format(self.first_name, self.last_name)