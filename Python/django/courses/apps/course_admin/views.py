#app course_admin views.py
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import Course, Description
# This will handle /
def index(request):
	courses = Course.objects.all()
	return render(request,'course_admin/index.html', {'courses': courses})

#This will handle POST to /new/
def new(request):
	if request.method == "POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			print request.POST['description']
			courses = Course.objects.all()
			return render(request,'course_admin/index.html', {'courses': courses,"name":request.POST['name'],"description":request.POST['description']})
		else:
			course = Course.objects.create(name=request.POST['name'])
			desc = Description.objects.create(desc=request.POST['description'], course=course)
	else:
		#Should never happen
		print "new --- Unexpected request method received:", request.method
	return redirect(reverse('course_admin_index'))

#This will handle /destroy/<id>/ and POST to /destroy/
def destroy(request, id=''):
	try:
		if request.method == "POST":
			if 'yes' in request.POST:
				course = Course.objects.get(id=request.POST['id'])
				print "deleting"
				course.delete()
		else:
			course = Course.objects.get(id=id)
			return render(request,'course_admin/destroy.html', {'course': course})
	except Exception as e:
			#Should not get here. Print error and redirect home.
			print '%s (%s)' % (e.message, type(e))
	return redirect(reverse('course_admin_index'))