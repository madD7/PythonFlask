import os
from flask import Flask, render_template, url_for, redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from forms import AddForm, DeleteForm, AddOwnerForm


### Setup Flask Application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'        # Secret key for forms

### SQL Database Section
### Setup SQL config for db
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)        # Setup db
Migrate(app, db)            # Do migration

# Register blueprints. Must be defined after the db setup
from myProject.puppies.views import puppies_blueprint
from myProject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
