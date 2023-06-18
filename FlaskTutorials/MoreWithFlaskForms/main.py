from flask import (Flask, render_template,
                   session, redirect, url_for)
from flask_wtf import FlaskForm  # Inherit class to create forms



"""
Almost every HTML form field has a corresponding wtforms class.
wtforms also has validators. 
Validators can perform check on the form data,
    eg: requiring a field to be filled.
"""
from wtforms import (StringField, SubmitField, SelectField, TextAreaField,
                     BooleanField, DateTimeField, RadioField)
from wtforms.validators import DataRequired

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

Using Flask's session object to grab info provided 
in the form and pass it to another template.
"""

app = Flask(__name__)

# Configure a secret key for csrf (Cross site request forgery) security
# Any string can be configured as secret key in config dict.
# We can set up secret key as an environment variable so that the key is not readable.
app.config['SECRET_KEY'] = 'mySecretKey'


class HomeForm(FlaskForm):
    """
    My sample Form class, inherits FlaskForm class.
    """
    # attributes that will be sent to template
    pup_breed = StringField("What breed is the pup?",  # string for label
                            validators=[DataRequired()])  # pass new instance of DataRequired.
    # Validator=DataRequired() means, this field must be compulsorily filled to submit the form

    vaccinated = BooleanField("Is the pup vaccinated?")
    mood = RadioField("Choose pup's mood:",
                      choices=[('mood_one', 'Happy'),
                               ('mood_two', 'Playful'),
                               ('mood_three', 'Calm')])
    # choices is a list of tupple pairs => value,label
    # value - seen in backend, label - seen by user on frontend
    # Check values displayed on the 'thankyou' page.

    food_choice = SelectField("Select pup's fav food: ",
                              choices=[('chi', 'Chicken'),
                                       ('pdg', 'Pedigree'),
                                       ('dgb', 'Dog Biscuits')])

    feedback = TextAreaField()
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
        """
            a session is just a time interval from when a client
            logs in upto until when client logs out
            As the session is imported, we have the session live for
            that particular user and hence DON'T need to pass it.
            session can be used in html.
        """
        session['breed'] = form.pup_breed.data
        session['vaccinated'] = form.vaccinated.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # when form is filled, redirect to 'thankyou' view.
        return redirect(url_for('thankyou'))

    # if form is not filled, render home.html page.
    return render_template('home.html', form=form)
# End of home()


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
