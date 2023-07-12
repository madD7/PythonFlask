import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# For migrating updates in the Flask model (python class mapped to db Table)
from flask_migrate import Migrate
"""
For Migration, Perform following 4 steps:
1. Set environment variable FLASK_MIGRATE=<python_app_script>.py
2. flask db init
3. flask db migrate -m "Some message"
4. flask db upgrade
"""


# Get the directory where the main.py is.
# We will build our DB in this directory.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connect Flask to DB
# set config for DB location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Don't track every single modification in DB

db = SQLAlchemy(app)

Migrate(app, db)    # To connect app to database, for migrating

# Set up a model (i.e. table in out DB). Create a class
class Puppy(db.Model):
    # A default table name is provide depending upon class name.
    # Overriding the default table name
    __tablename__ = 'puppies'

    # Primary key column
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)          # Added for migration demo.

    # Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # String representation of Object
    def __repr__(self):
        return f"Puppy: {self.name} is of breed{self.breed} & is {self.age} year(s) old."
