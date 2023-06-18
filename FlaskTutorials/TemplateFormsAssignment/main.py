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

@app.route('/result')
def result():
    """
    If the Username passes 3 conditions:
        it has atleast one lower case alphabet
        it has atleast one upper case alphabet
        the last character is a number
    then, it is success.
    Else test fails.
    :return: Rendered Html page.
    """
    # Check the html signup page, inputs
    username = request.args.get('username')   # <input name="firstname"> -- in home.html

    conditions = {'isLower': False, 'isUpper': False, 'isNumeric': False}

    for c in username:
        if c.islower():
            conditions['isLower'] = True

        if c.isupper():
            conditions['isUpper'] = True

    if c[-1].isnumeric():
        conditions['isNumeric'] = True

    return render_template('result.html', conditions=conditions)
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
