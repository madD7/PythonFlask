from flask import Blueprint, render_template, redirect, url_for, flash
from myProject import db
from myProject.models import Owner
from myProject.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        owner = form.owner_name.data
        pup_id = form.pup_id.data
        # pup = Puppy.query.get(pup_id)
        new_owner = Owner(owner, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        flash("Owner details saved.")
        return redirect(url_for('puppies.list'))

    return render_template('addOwner.html', form=form)
