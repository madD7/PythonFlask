import os
from flask import Flask, render_template, url_for, redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddForm, DeleteForm, AddOwnerForm


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
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"{self.owner.name} is owner of Puppy {self.name}. Pup Id: {self.id}."
        else:
            return f"Puppy {self.name} has no owner yet. Pup Id: {self.id}."


class Owner(db.Model):
    __tablename__ = 'owner'
    name = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id


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


@app.route('/addOwner', methods=['GET', 'POST'])
def addOwner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        owner = form.owner_name.data
        pup_id = form.pup_id.data
        # pup = Puppy.query.get(pup_id)
        new_owner = Owner(owner, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        flash("Owner details saved.")
        return redirect(url_for('list_puppies'))

    return render_template('addOwner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)