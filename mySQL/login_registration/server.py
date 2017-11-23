from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# Import regular expression module used to validate email addresses
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'users')
# This route handles the main/login page
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		try:
			user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
			query_data = { 'email': request.form['email'] }
			user = mysql.query_db(user_query, query_data) # user will be returned in a list
			if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
				# Successful login. Set session id
				session['id'] = user[0]['id']
				flash(u"You successfully logged in.", 'success')
				return render_template('/status.html')
			else:
				flash(u"That email/password combination did not work. Please try again.", 'error')
		except:
			flash(u"There was something wrong with that request.", 'error')
	return render_template('/login.html')

# This route handles create account page
@app.route('/create_account', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		error = False
		try:
			# Check if email already in db
			query = "SELECT COUNT(id) AS count from user where email like :email"
			email_exists = mysql.query_db(query, {'email':request.form['email']})
			if (email_exists[0]["count"] > 0):
				flash('There is already an account with email address ' + request.form['email'] + '.', 'error')
				return render_template("create_account.html")
			# Validate form fields.
			if len(request.form['first_name']) < 2:
				error = True
				flash(u"First name must have at least 2 characters", 'error')
			if len(request.form['last_name']) < 2:
				error = True
				flash(u"Last name must have at least 2 characters", 'error')
			if not EMAIL_REGEX.match(request.form['email']):
				error = True
				flash(u"Please enter a valid email address.", 'error')
			if len(request.form['password']) < 8:
				error = True
				flash(u"Password must have at least 8 characters.", 'error')
			elif request.form['password'] != request.form['confirm_password']:
				error = True
				flash(u"Password and Confirm Password must match.", 'error')
			if not error:
				# now we insert the new user into the database
				insert_query = "INSERT INTO user (email, first_name, last_name, pw_hash, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW() ,NOW())"
				query_data = { 'email': request.form['email'],
							   'first_name': request.form['first_name'],
							   'last_name': request.form['last_name'],
							   'pw_hash': bcrypt.generate_password_hash(request.form['password']) }
				mysql.query_db(insert_query, query_data)
				flash(u"Account successfully created!", 'success')
				return render_template("login.html")
		except:
			flash("There was something wrong with that request.", 'error')
	return render_template('/create_account.html')
app.run(debug=True)