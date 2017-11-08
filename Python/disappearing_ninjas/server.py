from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/', strict_slashes=False)
def index():
	return render_template("index.html")
# this route will handle our form submission
@app.route('/ninja', defaults={"color": ""}, strict_slashes=False)
@app.route('/ninja/<color>', strict_slashes=False)
def result(color):
	return render_template("ninja.html", color=color)
app.run(debug=True) # run our server