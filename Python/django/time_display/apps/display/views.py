from django.shortcuts import render, HttpResponse, redirect
import datetime
# the index function is called when root is visited
def index(request):
	dt = datetime.datetime.now().strftime("%b %d, %Y")
#	date = "test"
	tm = datetime.datetime.now().strftime("%I:%M %p")
	tm = tm.upper()
	context = {"date":dt,"time":tm}
	return render(request,'display/index.html', context)
