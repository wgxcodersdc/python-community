"""
tutorial_4.py

Contents:
	This is a very basic flask application that will 
	read and return some data from a sqlite database

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

from flask import Flask, make_response, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy


# make your Flask application that is the name of this file (eg, tutorial_4.py)
app = Flask(__name__)

# apps with POST should use a secret key to prevent cross-site request forgeries
# you'd want to read this in from your environment variables -- don't store in git!
app.config['SECRET_KEY'] = 'my-secret-key'


# database
BASE_DIR = os.path.dirname(__file__)
DATABASE = 'database/data.sqlite'
database_path = os.path.join(BASE_DIR, DATABASE)

# sqlAlchemy is looking for specific application context keys
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------
# database models
# ---------------
class Employee(db.Model):
	"""
	Represents an employee at the company
	"""
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), unique=True, nullable=False)
	last_name = db.Column(db.String(80), unique=True, nullable=False)

	department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
	department = db.relationship('Department', backref=db.backref('employees', lazy=True))

	def __repr__(self):
		return '<Employee %r %r>' % (self.first_name, self.last_name)


class Department(db.Model):
	"""
	Represents a department at the company
	"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)

	def __repr__(self):
		return '<Dept %r>' % self.name


def _serialize_model(model, backrefs=None):
	"""
	Serialize the model instance into a dictionary. 
	If backrefs, include that data in the dictionary.
	"""
	backrefs = [] if not backrefs else backrefs

	ret = {c.name: getattr(model, c.name) for c in model.__table__.columns}
	
	for br in backrefs:
		# not going to work right if it isn't M:1 but that's ok for now.
		ret[br] = _serialize_list(getattr(model, br))

	return ret

def _serialize_list(query_list, backrefs=None):
	"""
	Return the query list as a list of dictionaries. 
	If backrefs, include that data in the dictionary response.
	"""
	return [_serialize_model(m, backrefs) for m in query_list]

# ---------------	
# end db models
# ---------------


# ---------------
# endpoints
# ---------------
@app.route("/employees", methods=['GET'])
@app.route("/employees/<int:employee_id>", methods=['GET'])
def employees(employee_id=None):
	"""
	Endpoint to return employee list or 
	info for a single employee by id
	"""
	if not employee_id:
		employee_data = _serialize_list(Employee.query.all())
	else:
		employee_data = _serialize_model(Employee.query.filter_by(id=employee_id).first())

	resp = jsonify(employee_data)
	return resp

@app.route("/departments", methods=['GET'])
@app.route("/departments/<string:department_name>", methods=['GET'])
def departments(department_name=None):
	"""
	Endpoint to return department data, including 
	the list of employees who work in the department. 

	Can return a single department by name.
	"""
	if not department_name:
		department_data = _serialize_list(Department.query.all(), backrefs=["employees"])
		department_data = {'departments': department_data, 'total': len(department_data)}
	else:
		department_data = _serialize_model(Department.query.filter_by(name=department_name).first(), backrefs=["employees"])

	return jsonify(department_data)


