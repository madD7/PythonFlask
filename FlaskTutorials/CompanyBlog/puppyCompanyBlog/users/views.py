from flask import flash, render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from puppyCompanyBlog import db
from puppyCompanyBlog.models import User, BlogPost
from puppyCompanyBlog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppyCompanyBlog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email_id.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Registration Successful.")
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Successful.')

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('core.home')

            return redirect(next)

    return render_template('login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))
