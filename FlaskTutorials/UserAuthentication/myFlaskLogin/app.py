from myProject import app, db
from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myProject.models import User
from myProject.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(emailid=form.emailid.data).first()

        # Check if the user exists
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully.')

            # if the user was trying to visit a page that requires login, flask with save that page as next
            # so that, upon successfully login, the user will be automatically redirected to that page.
            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(emailid=form.emailid.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registration!')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are Logged out!')
    return redirect(url_for('home'))


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
