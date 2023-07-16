import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddForm, DeleteForm


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


### Model for db
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy name: {self.name}. Id:{self.id}'


### View Functions
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_puppy():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_puppies'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_puppies():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def delete_puppy():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)       # Only one puppy must be returned as id is primary key
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_puppies'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)