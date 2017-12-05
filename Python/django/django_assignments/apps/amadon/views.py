from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
	return render(request,'index.html')

def checkout(request):
	return render(request,'checkout.html')

def buy(request):
	if 'number_items' not in request.session:
		request.session['number_items'] = 0
	if 'order_total' not in request.session:
		request.session['order_total'] = 0
	if 'total' not in request.session:
		request.session['total'] = 0
	if ('id' in request.POST) and ('quantity' in request.POST):
		#If we had a database, we would get the price from there.
		price = 0
		if int(request.POST['id']) == 1:
			price = 19.99
		elif int(request.POST['id']) == 2:
			price = 29.99
		elif int(request.POST['id']) == 3:
			price = 4.99
		elif int(request.POST['id']) == 4:
			price = 49.99
		else:
			#Should not be here
			print "buy: Received bad id", request.POST['id']
			return redirect("/amadon")
		request.session['order_total'] = (int(request.POST['quantity']) * price)
		request.session['total'] += (int(request.POST['quantity']) * price)
		request.session['number_items'] += int(request.POST['quantity'])
		request.session.modified = True
		return redirect("/amadon/checkout/")
	else:
		# Should not be here. Redirect to main page
		print "buy: Received bad request"
		return redirect("/amadon")

def clear(request):
	if 'number_items'  in request.session:
		del request.session['number_items']
	if 'total'  in request.session:
		del request.session['total']
	if 'order_total'  in request.session:
		del request.session['order_total']
	request.session.modified = True
	return redirect("/amadon")