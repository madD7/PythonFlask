from flask import Flask

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)


"""
The string parameter that we pass into decorator,
determines the url extension that will link to the function
otherwise known as a view.
"""

@app.route('/')
@app.route('/home')
def index():
    """
    :return: Html Header as string
    """
    return '<h1>Hello Puppy!</h1>'
# End of index()


@app.route('/info')
def info():
    """
    :return: Html Header as String
    """
    return '<h1>Puppies are cute!</h1>'
# End of info()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run()
