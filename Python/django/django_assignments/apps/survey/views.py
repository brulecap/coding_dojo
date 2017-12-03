from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request, content=''):
	return render(request,'index.html')

def process(request):
	error = False
	if request.method == 'POST':
		print request.POST['name']
		if  len(request.POST['name']) < 1:
			error = True
			messages.error(request, 'Please enter a name.')
		if len(request.POST['comment']) < 1:
			error = True
			messages.error(request, 'Please enter a comment.')
		if len(request.POST['comment']) > 120:
			error = True
			messages.error(request, 'Your comment was too long. Could you shorten it to at most 120 characters?')
		# Create a dictionary to pass to the result template
		form_content = {"name":request.POST['name'],
						"comment":request.POST['comment'],
						"language":request.POST['language'],
						"location":request.POST['location']}
		if not error:
			if 'submitted' not in request.session:
				request.session['submitted'] = 1
			else:
				request.session['submitted'] += 1
			return render(request, "result.html", form_content)
		else:
			#Form did not validate. Render index and display flash messages
			return redirect("/survey", form_content)
	#Did not get here from a post. Redirect to survey page
	return redirect("/survey")
