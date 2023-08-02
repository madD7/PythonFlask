# This __init__ file will hold organisational logic - connecting blueprints,
# connecting login manager & connecting everything together.
# This will help organise.
from flask import Flask

app = Flask(__name__)

from puppyCompanyBlog.core.views import core

app.register_blueprint(core)
