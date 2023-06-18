import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Get the directory where the main.py is.
# We will build our DB in this directory.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connect Flask to DB
# set config for DB location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Don't track every single modification in DB

db = SQLAlchemy(app)


# Set up a model (i.e. table in out DB). Create a class
class Puppy(db.Model):
    # A default table name is provide depending upon class name.
    # Overriding the default table name
    __tablename__ = 'puppies'

    # Primary key column
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # String representation of Object
    def __repr__(self):
        return f"Puppy: {self.name} is {self.age} year(s) old."
