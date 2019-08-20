"""
tutorial_2.py

Contents:
	This is a very basic flask application that will 
	return data population data about states when called.

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
import os
import json
import csv

from flask import Flask, make_response, jsonify, request


# code if the server can't find something
HTTP_NOT_FOUND = 404


# base directory of this file
# eg, /home/ssyd/Development/women_who_code/intro_to_flask
BASE_DIR = os.path.dirname(__file__)


# path to our states file that is inside of the intro_to_flask directory
STATES_FILE = "data/state_population_data.csv"


# make your Flask application that is the name of this file (eg, tutorial_2.py)
app = Flask(__name__)


# ----------------------------------
# helper functions for our flask app
# ----------------------------------
def _load_states_data_from_csv():
	"""
	Read in and return the states_data from the csv file as a nested list like: 
		[
			['AL', 'Alabama', '1,000', '2,000'],
			['AZ', 'Arizona', '500', '600'],
			...
		]
	"""
	states_path = os.path.join(BASE_DIR, STATES_FILE)

	with open(states_path, newline="\n") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

		# trick to skip the header row [state,population_2010,population_2018]
		next(csv_reader)

		# get a nested list of state data
		states_data = list(csv_reader)

		return states_data


def _states_data_list_to_dict(states_data):
	"""
	Given a nested list of states data that looks like:
		[
			['AL', 'Alabama', '1,000', '2,000'],
			['AZ', 'Arizona', 500', '600'],
			...
		]
	Return the dictionary that looks like:
		{
			'AL': {'name': 'Alabama', '2010_pop': 1000, '2018_pop': 2000},
			'AZ': {'name', 'Arizona', 2010_pop': 500, '2018_pop': 600}
		}
	"""
	states_dict = {}
	for single_state_data in states_data:

		state_abbreviation = single_state_data[0]
		state_name = single_state_data[1]
		pop_2010_str = single_state_data[2]
		pop_2018_str = single_state_data[3]

		# return integers for our clients -- get rid of commas
		pop_2010 = int(pop_2010_str.replace(",", ""))
		pop_2018 = int(pop_2018_str.replace(",", ""))

		states_dict[single_state_data[0]] = {
			"abbreviation": state_abbreviation,
			"name": state_name, 
			"2010_pop": pop_2010, 
			"2018_pop": pop_2018
		}

	return states_dict


def _states_data_list_to_dict_v2(states_data, population_filters):
	"""
	Given a nested list of states data that looks like:
		[
			['AL', 'Alabama', '1,000', '2,000'],
			['AZ', 'Arizona', 500', '600'],
			...
		]
	AND a population_filters dictionary that looks like:
		{"2010_pop_lt": 600}

	Use the population_filters to remove any values that don't meet 
	our criteria. 
	An empty filter will return all results.

	Then return the dictionary that looks like:
		{
			'AZ': {'name': 'Arizona', '2010_pop': 500, '2018_pop': 600},
		}
	"""	
	filter_2010_lt = population_filters.get('2010_pop_lt')	
	filter_2018_lt = population_filters.get('2018_pop_lt')

	states_dict = {}
	for single_state_data in states_data:

		state_abbreviation = single_state_data[0]
		state_name = single_state_data[1]
		pop_2010_str = single_state_data[2]
		pop_2018_str = single_state_data[3]

		# return integers for our clients -- get rid of commas
		pop_2010 = int(pop_2010_str.replace(",", ""))
		pop_2018 = int(pop_2018_str.replace(",", ""))

		# apply filtering
		keep_data = True
		if filter_2010_lt and pop_2010 >= filter_2010_lt:
			keep_data = False
			
		if filter_2018_lt and pop_2018 >= filter_2018_lt:
			keep_data = False

		# add state if it meets our filter criteria
		if keep_data:
			states_dict[single_state_data[0]] = {
				"abbreviation": state_abbreviation,
				"name": state_name, 
				"2010_pop": pop_2010, 
				"2018_pop": pop_2018
			}

	return states_dict


# ----------------------------------
# flask endpoints
# ----------------------------------
# let's make an endpoint that will read in state data from a csv file
@app.route("/states")
def state_list():
	"""
	Return a dictionary of states population data as json. 
	"""
	# get the nested list of states from the csv
	states_list = _load_states_data_from_csv()

	# build a dictionary of the data
	states_dict = _states_data_list_to_dict(states_list)

	# turn the state_data into json string
	json_data = json.dumps(states_dict)

	# we could return that json_data as a big string... 
	# eg, return json_data
	# but it is better to tell the client that we are sending back json using the mimetype
	resp = make_response(json_data)
	resp.mimetype = 'application/json'

	return resp

# let's update the last endpoint so that it also supports query parameters
@app.route("/statesv2")
def state_list_v2():
	"""
	Return a dictionary of states population data as json. 

	Supports basic queries like ?2010_pop_lt=2000 or ?2018_pop_lt=1000 
	to filter down the amount of data returned.
	"""
	# supported filters. just ignore filters we don't know about.
	population_filter_keys = ["2010_pop_lt", "2018_pop_lt"]

	print('request args')
	print(request.args)

	population_filters = {}
	for _filter in population_filter_keys:
		filter_value = request.args.get(_filter)
		if filter_value and filter_value.isdigit():
			population_filters[_filter] = int(filter_value)

	# get the nested list of states from the csv
	states_list = _load_states_data_from_csv()

	# build a dictionary of the data. this version takes the filters, too.
	states_dict = _states_data_list_to_dict_v2(states_list, population_filters)
	print("got valid filters: {}".format(population_filters))
	print("states count: {}".format(len(states_dict)))

	# turn the state_data into json string
	json_data = json.dumps(states_dict)

	# we could return that json_data as a big string... 
	# eg, return json_data
	# but it is better to tell the client that we are sending back json using the mimetype
	resp = make_response(json_data)
	resp.mimetype = 'application/json'

	return resp


@app.route('/states/<state_abbr>')
def state_detail(state_abbr):
	"""
	Return a dictionary with information about a given state_abbr as json
	"""
	# get the nested list of states from the csv
	states_list = _load_states_data_from_csv()

	# build a dictionary of the data
	states_dict = _states_data_list_to_dict(states_list)

	# return the specific data for <state_abbr>. 
	state_data = states_dict.get(state_abbr.upper(), {})

	# this is another way to make the json response
	resp = jsonify(state_data)

	if not state_data:
		# no such state. 404 not found.
		resp.status_code = HTTP_NOT_FOUND

	return resp

