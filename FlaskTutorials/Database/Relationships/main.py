import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Get the directory where the main.py is.
# We will build our DB in this directory.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connect Flask to DB
# set config for DB location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Don't track every single modification in DB

db = SQLAlchemy(app)
Migrate(app, db)  # To connect app to database, for migrating


# Toys from puppy
class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)

    # Puppy object tablename is: puppies. thus, puppies.id
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # Connecting one (puppy) to many (toys)
    # 1st parameter - relation of toys column with Toy object
    # 2nd parameter - back refrence to connect toy with puppy
    # 3rd parameter - Lazy parameter determines how the related
    #                   objects get loaded when querying through relationships.
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    # Connecting one (puppy) to One (owner)
    # Uselist=False indicates, that one puppy has only one owner. One to One relation.
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return (f"{self.owner.name} is owner of Puppy {self.name}.")
        else:
            return (f"Puppy {self.name} has no owner yet.")

    def report_toys(self):
        print(f"{self.name} has toys: ")
        for t in self.toys:
            print(t.item_name)
