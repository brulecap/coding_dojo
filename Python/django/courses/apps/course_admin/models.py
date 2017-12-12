# app course_admin models.py
from __future__ import unicode_literals
from django.db import models
class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 6:
			errors["first_name"] = "Course name should be more than 5 characters."
		if len(postData['description']) < 16:
			errors["last_name"] = "Description should be more than 15 characters."
		return errors
class Course(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()
	def __repr__(self):
		return "<Course object: {}>".format(self.name)
class Description(models.Model):
	desc = models.TextField()
	course = models.OneToOneField(Course, related_name="descriptions")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Description object: {}>".format(self.desc)