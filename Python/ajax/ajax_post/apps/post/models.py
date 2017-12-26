# app login_registration models.py
from __future__ import unicode_literals
from django.db import models

class Note(models.Model):
	note = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<User object: {}>".format(self.note)