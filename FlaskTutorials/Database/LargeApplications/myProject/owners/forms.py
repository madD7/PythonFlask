from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    owner_name = StringField('Name of the Owner: ')
    pup_id = IntegerField('Puppy ID: ')
    submit = SubmitField('Add Owner Details')
