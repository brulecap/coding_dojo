'''
Assignment: Ninja Gold
You're going to create a mini-game that helps a ninja make some money! When you start the
game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house,
casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or
LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and
to display past activities of this ninja.

Guidelines

Refer to the wireframe below.
Have the four forms appear when the user goes to http://localhost:5000.
For the farm, your form would look something like
<form action="/process_money" method="post">
  <input type="hidden" name="building" value="farm" />
  <input type="submit" value="Find Gold!"/>
</form>

In other words include a hidden value in the form and have each form submit the form information 
o /process_money.
Have /process_money determine how much gold the user should have.
You should only have 2 routes -- '/' and '/process_money'
'''

from flask import Flask, render_template, request, redirect, session
import random
import datetime
random.seed()
app = Flask(__name__)
# Provide secret key... Used os.urandom(24)
app.secret_key = 'b\xa7\xc8\x1b}\x93\xf9\x18E\x9a]\x9f\x14\x1e\x80\xc4\x05\xb2\x1c\xfb\xb4\x12f\xc8'

'''
Create buildings dictionary. key is the name of the building and the tuple associated with the
key is the min value followed by the max_value available in that building.
'''
buildings = {"farm":(10,20), "cave":(5,10), "house":(2,5), "casino":(-50,50)}

'''
This route will handle the initial page and reset when playing again
'''
@app.route('/')
def index():
	session['gold'] = 0
	session['activities'] = []
	return render_template("index.html")

#This route handles processing which building was selected
@app.route('/process_money', methods=['POST'])
def generate_gold():
	if request.form['building'] in buildings:
		gold_earned = random.randint(buildings[request.form['building']][0], buildings[request.form['building']][1])
	else:
		'''
			Should never make it here. Only way we could is via a hack or an error in code.
			Print error and return
		'''
		print "Unknown building."
		return render_template("index.html")
	session['gold'] += gold_earned
	#Get date time string for use in output
	date_time_now = datetime.datetime.now().strftime("%y/%m/%d %I:%M %p").lstrip("0").replace(" 0", " ").lower()
	if gold_earned >= 0:
		output_string = '<p class="green">Earned ' + str(gold_earned) + ' gold' + ("s" if gold_earned!=1 else "") + ' from the ' + request.form['building'] + '! (' + date_time_now + ')</p>'
	else:
		output_string = '<p class="red">Entered a ' + request.form['building'] + ' and lost ' + str(gold_earned) + ' gold' + ("s" if gold_earned!=1 else "") + '... Ouch.. (' + date_time_now + ')</p>'
	session['activities'].insert(0, output_string)
	return render_template("index.html")

app.run(debug=True) # run our server