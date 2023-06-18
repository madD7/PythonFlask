from flask import Flask, render_template
from flask_wtf import FlaskForm             # Inherit class to create forms
from wtforms import StringField, SubmitField

"""
Using flask_wtf library and  wtforms package to create forms from python script.

1. Configure a secret key for security.
2. Create wtform class
    create fields for each part of the form.
3. setup a view function
    Add methods - GET, POST
    Create instance of Form class
    Handle Form submission

In this example, we will create form class and view functions in same script.
"""

app = Flask(__name__)

# Configure a secret key for csrf security
# csrf = Cross site request forgery.

# Any string can be configured as secret key in config dict.
# We will later learn better ways to configure secret key.
# We can set-up secret key as an environment variable so that the key is not readable.
app.config['SECRET_KEY'] = 'mySecretKey'


class HomeForm(FlaskForm):
    """
    My sample Form class, inherits FlaskForm class.
    """
    # attributes that will be sent to template
    pup_breed = StringField("What breed is the pup?")     # put string for label
    submit = SubmitField("Submit")


# View Functions
# methods allow us to pass in the form to the template
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    breed = False
    form = HomeForm()

    # Check if form is valid on submission
    if form.validate_on_submit():
        # if valid, grab data
        breed = form.pup_breed.data
        form.pup_breed.data = ''

    return render_template('home.html',
                           form=form, breed=breed)
# End of home()


if __name__ == "__main__":
    app.run(debug=True)

