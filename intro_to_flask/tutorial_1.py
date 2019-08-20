"""
tutorial_1.py

Contents:
	This is a very basic flask application that will 
	return a string when the url is called.

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
# import the flask base class
from flask import Flask


# make your Flask application that is the name of this file (eg, tutorial_1.py)
app = Flask(__name__)


# decorate this function so that flask knows that calls to <base_url>/ will come here
@app.route("/")
def index():
	"""
	Return a basic message from the base url
	"""
	message = "Hello, world! I'm using flask! Yay!"
	return message
