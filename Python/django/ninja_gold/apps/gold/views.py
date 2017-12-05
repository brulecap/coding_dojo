from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
#random used to determine how much many was earned or lost
import random
import datetime

'''
Create buildings dictionary. key is the name of the building and the tuple associated with the
key is the min value followed by the max_value available in that building.
'''
buildings = {"farm":(10,20), "cave":(5,10), "house":(2,5), "casino":(-50,50)}

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activities' not in request.session:
		request.session['activities'] = []
	return render(request,'index.html')

def generate_gold(request, building=''):
	print 'generate_gold', building
	if request.method == "POST":
		try:
			if building in buildings:
				gold_earned = random.randint(buildings[building][0], buildings[building][1])
			else:
				'''
					Should never make it here. Only way we could is via a hack or an error in code.
					Print error and return
				'''
				print "Unknown building:", building
				return redirect("/")
			request.session['gold'] += gold_earned
			#Get date time string for use in output
			date_time_now = datetime.datetime.now().strftime("%y/%m/%d %I:%M %p").lstrip("0").replace(" 0", " ").lower()
			if gold_earned >= 0:
				output_string = '<p class="green">Earned ' + str(gold_earned) + ' gold' + ("s" if gold_earned!=1 else "") + ' from the ' + building + '! (' + date_time_now + ')</p>'
			else:
				output_string = '<p class="red">Entered a ' +building + ' and lost ' + str(gold_earned) + ' gold' + ("s" if gold_earned!=1 else "") + '... Ouch.. (' + date_time_now + ')</p>'
			request.session['activities'].insert(0, output_string)
		except Exception as e:
			print(e)
	return redirect("/")

def reset(request):
	if 'gold' in request.session:
		del request.session['gold']
	if 'activities' in request.session:
		del request.session['activities']
#	request.session.modified = True
	return redirect("/")