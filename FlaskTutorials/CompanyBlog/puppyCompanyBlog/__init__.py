# This __init__ file will hold organisational logic - connecting blueprints,
# connecting login manager & connecting everything together.
# This will help organise.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

## DB setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


## Login Config
login_manager = LoginManager()
login_manager.init_app(app)

# Users Blueprint will have login view, that is connected here.
login_manager.login_view = 'users.login'

from puppyCompanyBlog.core.views import core
from puppyCompanyBlog.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(error_pages)

