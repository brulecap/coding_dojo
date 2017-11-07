from flask import Flask, render_template, request, redirect, session, flash
# the "re" module will let us perform some regular expression operations
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
app = Flask(__name__)
# Provide secret key... Used os.urandom(24)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
# create a regular expression object that we can use to validate email addresses
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")
# this route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
	error = False
	# validate first name, not empty and no numbers
	if  len(request.form['first_name']) < 1 or not request.form['first_name'].isalpha():
		error = True
		flash(u"First name is required and can not contain a number.", 'error')
	# validate last name, not empty and no numbers
	if  len(request.form['last_name']) < 1 or not request.form['last_name'].isalpha():
		error = True
		flash(u"Last name is required and can not contain a number.", 'error')
	# use regex to validate email.
	if not EMAIL_REGEX.match(request.form['email']):
		error = True
		flash("Please input a valid email address.", 'error')
	# Perform a try/excpetion because datetime.strptime throws an exception if the string is not properly formatted
	try:
		if datetime.strptime(request.form['birthday'], "%Y-%m-%d") > datetime.now() - relativedelta(years=3):
			error = True
			flash(u"You are too young. Please have you parents register.", 'error')
	except ValueError:
		error = True
		flash(u"Please select your birthday using the date selector.", 'error')
	# Validate password, at least one number, one uppercase, and 8 or more characters.
	if len(request.form['password']) < 8 or not bool(re.search(u'\d', request.form['password'])) or request.form['password'].islower() or request.form['password'] != request.form['confirm']:
		error = True
		flash(u"Password and confirmation password must match, contain at least 8 characters, have at least one uppercase value and 1 numeric value.", 'error')
	# Create a dictionary to pass to the appropriate template template
	# This allows us to repopulate some fields so the user can see a mistake and/or won't have to
	# retype information.
	form_content = {"first_name":request.form['first_name'],
					"last_name":request.form['last_name'],
					"email":request.form['email'],
					"birthday":request.form['birthday']}
	if not error:
		return render_template("result.html", results=form_content)
	else:
		#Form did not validate. Render index and display flash messages
		return render_template("index.html", results=form_content)
app.run(debug=True) # run our server