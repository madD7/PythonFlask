from myProject import app, db
from flask import render_template
from myProject.models import Puppy, Owner


@app.route('/')
def home():
    return render_template('home.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
