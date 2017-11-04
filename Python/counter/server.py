from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
	return render_template("index.html")

@app.route('/double')
def double():
	# Add 1 here and then another 1 will be added on the redirect
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
	return redirect("/")

@app.route('/reset')
def reset():
	# Set to 0 here and then 1 will be added on the redirect
	session['count'] = 0
	return redirect("/")
app.run(debug=True) # run our server