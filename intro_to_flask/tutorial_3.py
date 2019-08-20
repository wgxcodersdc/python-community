"""
tutorial_3.py

Contents:
	This is a very basic flask application that will 
	return word frequencies from a string when a user 
	POSTs a string to the endpoint.

Usage:
	To start your flask web app on the command line, you need to do two steps
	1. Tell flask the name of your FLASK_APP
	2. Start flask program for local development
		-- flask will run on localhost on port 5000

	Mac
	-- open a terminal window
	-- cd to your flask directory
	-- in the terminal type:
		export FLASK_APP=tutorial.py
		flask run

	Windows
	-- open a cmd window
	-- cd to your flask directory
	-- in the cmd window type
		C:\path\to\app>set FLASK_APP=tutorial.py
		flask run

	Open your browser. Go to http://127.0.0.1:5000/
""" 
from collections import Counter
import re

from flask import Flask, make_response, jsonify, request, render_template


# make your Flask application that is the name of this file (eg, tutorial_3.py)
app = Flask(__name__)

# apps with POST should use a secret key to prevent cross-site request forgeries
# you'd want to read this in from your environment variables -- don't store in git!
app.config['SECRET_KEY'] = 'my-secret-key'


def _calculate_word_frequencies(input_string, ignore_case=True):
	"""
	Very basic function to return a dictionary of words to counts for the input_string. 
	If ignore_case, "Cat" == "cat". Else "Cat" != "cat".
	
	Given "The cat likes to watch the birds.", ignore_case=True.
	Return: 
	{
		"the": 2,
		"cat": 1,
		"likes": 1,		
		"to": 1,
		"watch": 1,
		"birds": 1
	}
	"""
	if ignore_case:
		input_string = input_string.lower()

	# remove basic punctuation
	clean_string = re.sub(r"[,?\.!\(\)\n\t\r]", "", input_string, flags=re.I)

	# remove extra white space
	clean_string = re.sub(r" +", ' ', clean_string)

	# build the dictionary
	words = Counter(clean_string.split(" "))
	return words


# let's make an endpont that will just return information about a string that we 
# have stored in the application
@app.route("/frequenciesv1", methods=['GET'])
def frequenciesv1():
	"""
	Endpoint to return word count frequencies in a string 
	that is already stored in the view function.

	GET .../frequencies
		Return information about the input string stored in this function
		input_string = "My test sentence!"

		Return: {"my": 1, "test": 1, "sentence": 3}
	"""
	# http://flask.pocoo.org/docs/1.0/foreword/#what-does-micro-mean
	paragraph = """
	“Micro” does not mean that your whole web application has to fit into a 
	single Python file (although it certainly can), nor does it mean that 
	Flask is lacking in functionality. The “micro” in microframework means 
	Flask aims to keep the core simple but extensible. Flask won’t make 
	many decisions for you, such as what database to use. Those decisions 
	that it does make, such as what templating engine to use, are easy to 
	change. Everything else is up to you, so that Flask can be everything 
	you need and nothing you don’t.
	"""
	print(paragraph)

	word_counts = _calculate_word_frequencies(paragraph)

	resp = jsonify(word_counts)
	return resp


# let's make an endpoint that will take an input and return information about the string we posted
@app.route("/frequencies", methods=['GET', 'POST'])
def frequencies():
	"""
	Endpoint to return word count frequencies in an input string 
	that is provided in the request.

	GET .../frequencies
		Return form for posting information to the endpoint

	POST .../frequencies
		Client posts:
		{
			"input_string": "My test sentence Sentence sentence.",
			"ignore_case": true
		}

		Return: {"my": 1, "test": 1, "sentence": 3}
	"""
	if request.method == 'POST':
		print(request.method)
		print(request.form)
		# return frequencies in json
		input_string = request.form.get('input_string', '')
		ignore_case = request.form.get('ignore_case', False)

		frequencies = _calculate_word_frequencies(input_string, ignore_case)
		resp = jsonify(frequencies)

	else:
		# display the form for the user
		# by default, flask will look in the template subdirectory

		# we should use flaskWTF and set hidden for csrf, but we'll keep it simple
		resp = render_template('frequencies.html')

	return resp

