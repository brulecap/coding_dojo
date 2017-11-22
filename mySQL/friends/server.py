from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'friendsdb')
# This route handles the main page
@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)
#This route handles add a friend
@app.route('/friends', methods=['POST'])
def create():
	try:
		if  len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or not EMAIL_REGEX.match(request.form['email']):
			flash(u"All fields are required and the email mus be valid. Please click Home below and try again.", 'error')
			return render_template('error.html')
		# Write query as a string.
		query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
		# We'll then create a dictionary of data from the POST data received.
		data = {
				'first_name': request.form['first_name'], 
				'last_name':  request.form['last_name'],
				'email': request.form['email']
				}
		# Run query, with dictionary values injected into the query.
		mysql.query_db(query, data)
	except:
		flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
		return render_template('error.html')				
	return redirect('/')
	# This route handles edit
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
	try:
		query = "SELECT * FROM friends WHERE id = :specific_id"
		# Then define a dictionary with key that matches :specific_id in query.
		data = {'specific_id': friend_id}
		# Run query with inserted data.
		friends = mysql.query_db(query, data)
		if len(friends) != 1:
			flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
			return render_template('error.html')
	except:
		flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
		return render_template('error.html')						
	# Friends should be a list with a single object,
	# so we pass the value at [0] to our template under alias friend.
	return render_template('edit.html', friend=friends[0])
# this route will handle the post request from the edit page
@app.route('/update', methods=['POST'])
def update():
	try:
		print request.form
		if  len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or not EMAIL_REGEX.match(request.form['email']):
			flash(u"All fields are required and the email mus be valid. Please click Home below and try again.", 'error')
			return render_template('error.html')
		query = """UPDATE friends 
				SET first_name = :first_name, last_name = :last_name, email = :email 
				WHERE id = :id"""
		print query
		data = {
				'first_name': request.form['first_name'], 
				'last_name':  request.form['last_name'],
				'email': request.form['email'],
				'id': request.form['id']
				}
		print data
		mysql.query_db(query, data)
	except:
		flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
		return render_template('error.html')				
	return redirect('/')
@app.route('/friends/delete', methods=['POST'])
def destroy():
	try:
		query = "select COUNT(id) AS num_friends FROM friends WHERE id = :id"
		count = mysql.query_db(query, {'id': request.form['id']})
		if count[0]['num_friends'] != 1:
			flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
			return render_template('error.html')		
		query = "DELETE from friends WHERE id = :id"
		mysql.query_db(query, {'id': request.form['id']})
	except:
		flash(u"Something was wrong with that request. Use the link below to return to the home page and try again.", 'error')
		return render_template('error.html')		
	return redirect('/')
app.run(debug=True)