from flask import Flask, render_template, request, redirect, session, flash
#import regular expression mmodule for validating email address
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# Provide secret key... Used os.urandom(24)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
# create a regular expression object that we can use to validate email addresses
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
#Create connection to emails database
mysql = MySQLConnector(app,'emails')
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")
# this route will handle our form submission and add the email address to the database
@app.route('/add_email', methods=['POST'])
def create_email():
	# Make sure email is valid
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid!", 'error')
		return render_template("index.html")
	# check if email already exists in database
	query = "SELECT COUNT(id) AS count from email_addresses where email_address like :address"
	email_exists = mysql.query_db(query, {'address':request.form['email']})
	if (email_exists[0]["count"] > 0):
		print email_exists[0]["count"]
		flash("Email address already in database!", 'error')
		return render_template("index.html")
	query = "INSERT INTO email_addresses (email_address, created_at, modified_at) VALUES (:address, NOW(), NOW())"
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, {'address':request.form['email']})
	flash("The email address (" + request.form['email'] + ") is a VALID email address! Thank you!", 'success')
	query = "SELECT id, email_address, modified_at FROM email_addresses"
	emails = mysql.query_db(query)
	# render success template
	return render_template("success.html", emails=emails)
# this route will handle our delete form submission
@app.route('/delete', methods=['POST'])
def delete_email():
	query = "DELETE FROM email_addresses where id = :delete_id"
	delete_list = request.form.getlist("id")
	for delete_id in delete_list:
		mysql.query_db(query, {'delete_id':delete_id})
#	print request.form
#	for key, value in request.form.iteritems():
#		print key, value
	return render_template('index.html')
app.run(debug=True) # run our server