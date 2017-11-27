from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime as dt
# Import regular expression module used to validate email addresses
import re
# Bcrypt is used for encrypting the password
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Two functions to provide time format in templates.
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

app.jinja_env.globals.update(suffix=suffix)
app.jinja_env.globals.update(custom_strftime=custom_strftime)

bcrypt = Bcrypt(app)
# Session secret key. Used os.urandom(24)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
# Email validation regular expression
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Make dadtabase connection
mysql = MySQLConnector(app,'walldb')

# This route handles the wall page
@app.route('/wall')
def wall():
	if not session.get('id'):
		return redirect('/')
# Tried to make one sql query... Got close but it has problems
#	message_query = """SELECT messages.message, messages.created_at AS message_date, messages.id,
#					   GROUP_CONCAT(CONCAT(comments.comment, ';', comments.created_at, ';', comments.id, ';', CONCAT(comment_user.first_name, ' ',comment_user.last_name)) SEPARATOR ':') AS comments,
#					   CONCAT(message_user.first_name, ' ',message_user.last_name) AS message_name
#					   FROM messages
#					   JOIN users AS message_user ON messages.user_id=message_user.id
#					   LEFT JOIN comments ON comments.message_id=messages.id
#					   LEFT JOIN users AS comment_user ON comment_user.id=comments.user_id ORDER BY messages.id, comments.id
#					   GROUP BY messages.message, messages.created_at, messages.id, message_user.first_name, message_user.last_name"""
	message_query = """SELECT messages.message, messages.created_at AS message_date, messages.id, concat(users.first_name, ' ',users.last_name) AS message_owner
				       FROM messages JOIN users on messages.user_id=users.id"""
	content = mysql.query_db(message_query)
	comment_query = """SELECT comments.comment, comments.created_at AS comment_date, concat(users.first_name, ' ',users.last_name) AS comment_owner
					   FROM comments
					   JOIN users ON comments.user_id=users.id
					   WHERE comments.message_id=:id"""
	for a in content:
		a['comments'] = []
		query_data = {'id':a['id']}
		message_comments = mysql.query_db(comment_query, query_data)
		a['comments'] = message_comments
		print a
	return render_template('/wall.html', content=content)

# This route handles the login/main page
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if session.get('id'):
		return redirect('/wall')
	if request.method == 'POST':
		try:
			user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			query_data = { 'email': request.form['email'] }
			user = mysql.query_db(user_query, query_data) # user will be returned in a list
			if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
				# Successful login. Set session id
				session['id'] = user[0]['id']
				session['first_name'] = user[0]['first_name']
				return redirect('/wall')
			else:
				flash(u"That email/password combination did not work. Please try again.", 'error')
		except:
			flash(u"There was something wrong with that request.", 'error')
	return render_template('/login.html')

# This route handles logging out
@app.route('/logout')
def logout():
	session.clear()
	return render_template('/login.html')

# This route handles create account page
@app.route('/create_account', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		error = False
		try:
			# Check if email already in db
			query = "SELECT COUNT(id) AS count from users where email like :email"
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
				insert_query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at, updated_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW(), NOW())"
				query_data = { 'email': request.form['email'],
							   'first_name': request.form['first_name'],
							   'last_name': request.form['last_name'],
							   'pw_hash': bcrypt.generate_password_hash(request.form['password']) }
				mysql.query_db(insert_query, query_data)
				return redirect('/wall')
		except:
			flash("There was something wrong with that request.", 'error')
	return render_template('/create_account.html')

# This route handles new messages
@app.route('/message', methods=['POST'])
def new_message():
	if not session.get('id'):
		return redirect('/')
	try:
		print request.form
		if request.form['type'] == "message":
			if len(request.form['message']) > 0:
				insert_query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
				query_data = { 'message': request.form['message'],
							   'user_id': session['id']}
				mysql.query_db(insert_query, query_data)
			else:
				flash("Message length greater than 0 required.", 'error')
		elif request.form['type'] == "comment":
			print 'hererererer'
			if len(request.form['comment']) > 0:
				insert_query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())"
				query_data = { 'comment': request.form['comment'],
							   'user_id': session['id'],
							   'message_id': request.form['message_id']}
				print query_data
				mysql.query_db(insert_query, query_data)
			else:
				flash("Comment length greater than 0 required.", 'error')
		else:
			flash("Unknown request made.", 'error')

	except:
			flash("There was something wrong with that request.", 'error')
	return redirect('/wall')

app.run(debug=True)