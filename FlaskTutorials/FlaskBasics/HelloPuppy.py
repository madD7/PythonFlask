from flask import Flask

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    """
    The string parameter that we pass into decorator,
    determines the url extension that will link to the function
    otherwise known as a view.
    :return: Html Header
    """
    return '<h1>Hello Puppy!</h1>'
# End of index()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run()
