from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")
# this route will handle our form submission
@app.route('/result', methods=['POST'])
def result():
	print "Got Post Info"
	# Create a dictionary to pass to the result template 
	form_content = {"name":request.form['name'],
					"comment":request.form['comment'],
					"language":request.form['language'],
					"location":request.form['location']}
	return render_template("result.html", survey_results=form_content)
app.run(debug=True) # run our server