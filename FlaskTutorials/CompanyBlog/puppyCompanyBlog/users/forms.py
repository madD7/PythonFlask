from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppyCompanyBlog.models import User


class LoginForm(FlaskForm):
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_passwd', message='Password must match.')])
    confirm_passwd = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email_id=field.data).first():
            raise ValidationError('Email has been already registered.')

    def check_email(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has been already registered.')


class UpdateUserForm(FlaskForm):
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed('jpg', 'png')])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email_id=field.data).first():
            raise ValidationError('Email has been already registered.')

    def check_email(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has been already registered.')

