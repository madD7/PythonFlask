from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from myProject.models import User


class LoginForm(FlaskForm):
    emailid = StringField('Email ID: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    # 1st arg is Label.
    emailid = StringField('Email ID: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])

    # EqualTo - we have to pass the actual attribute of the form that it needs to be equal to.
    password = PasswordField('Password: ',
                             validators=[DataRequired(),
                                         EqualTo('pass_confirm', message='Passwords must match.')])

    pass_confirm = PasswordField('Confirm Password: ',
                                 validators=[DataRequired(),
                                             EqualTo('pass_confirm', message='Passwords must match.')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The username is already taken.')






