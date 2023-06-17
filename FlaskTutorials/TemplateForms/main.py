from flask import Flask, render_template, request

# request is used to grab information from HTML Form.

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)

"""
Template Forms:

"""


@app.route('/')
@app.route('/home')
def home():
    """
    Home page
    :return: Rendered Html page
    """
    return render_template('home.html')     # Must match exactly with the filename
# End of index()


@app.route('/signup')
def signup():
    """
    Signup page
    :return: Rendered Html page
    """
    return render_template('signup.html')
# End of signup()


@app.route('/thankyou')
def thankyou():
    """
    Signup Successful. Thank You page.
    Once the user actually fills out the signup form, we technically have
    a live session with that user. We want the user signup information.
    We will 'request' for the user signup information.
    :return: Rendered Html page.
    """
    # Check the html signup page, inputs
    first = request.args.get('firstname')   # <input name="firstname"> -- in signup.html
    last = request.args.get('lastname')     # <input name="lastname">  -- in signup.html
    return render_template('thankyou.html', first=first, last=last)
# End of thankyou()


@app.errorhandler(404)
def page_not_found(e):
    """
    Special error handler page.
    Will be displayed whenever a wrong url is entered.
    :param e:
    :return: Error404 Html page.
    """
    return render_template('Error404.html')
# End of page_not_found()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run(debug=True)
