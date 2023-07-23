
# Configure os environment variables. required for using OAuth for local host.
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'

# Client id & Client secret must be setup with Google
# Client id & client secret can be passed as environment variables
# basically, must not be in code.
blueprint = make_google_blueprint(client_id='1088699797409-ffplpq7rfvpcc9fag5p0lhuqd77ia6i7.apps.googleusercontent.com',
                                  client_secret='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',
                                  offline=True, scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
def welcome():

    # this code will result to error if the welcome page is accessed without login.
    # this is just an example code. redirection can be written here.
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text  # Verify that response is not blank or empty. Response is json
    email = resp.json()["emails"][0]["value"]

    return render_template('welcome.html')


# to ensure that we dont get error when connecting to google blueprint
@app.route('/login/google')
@app.route('/login/google/authorized')
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text       # Verify that response is not blank or empty. Response is json
    email = resp.json()["emails"][0]["value"]
    print(f"Email:  {email}")

    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])


if __name__ == "__main__":
    app.run(debug=True)
