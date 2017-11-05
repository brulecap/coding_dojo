'''
Assignment: Great Number Game
Create a site that when a user loads it creates a random number between 1-100 and stores
the number in session. Allow the user to guess at the number and tell them when they are
too high or too low. If they guess the correct number tell them and offer to play again.

'''
from flask import Flask, render_template, request, redirect, session
import random
random.seed()
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purpose
'''
This route will handle the initial page and reset when playing again
'''
@app.route('/')
def index():
	session['number'] = random.randint(1, 100)
	return render_template("index.html")

#This route handles the guesses
@app.route('/guess', methods=['POST'])
def guess():
	print "I am here"
	if int(request.form['guess']) > session['number']:
		print "fuck lesser " ,request.form['guess'], session['number']
		return render_template("lesser.html")
	elif int(request.form['guess']) < session['number']:
		print "fuck greater then" , request.form['guess'], session['number']
		return render_template("greater.html")
	else:
		print "equals" ,request.form['guess'], session['number']
		return render_template("equal.html")

app.run(debug=True) # run our server