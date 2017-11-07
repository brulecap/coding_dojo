from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
# Provide secret key... Used os.urandom(24)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")
# this route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
	#Validate form inputs 
	error = False
	if  len(request.form['name']) < 1:
		error = True
		flash("Please enter a name.")
	if len(request.form['comment']) < 1:
		error = True
		flash("Please enter a comment.")
	if len(request.form['comment']) > 120:
		error = True
		flash("Your comment was too long. Could you shorten it to at most 120 characters?")
	# Create a dictionary to pass to the result template
	form_content = {"name":request.form['name'],
					"comment":request.form['comment'],
					"language":request.form['language'],
					"location":request.form['location']}
	if not error:
		return render_template("result.html", survey_results=form_content)
	else:
		#Form did not validate. Render index and display flash messages
		return render_template("index.html", survey_results=form_content)
app.run(debug=True) # run our server