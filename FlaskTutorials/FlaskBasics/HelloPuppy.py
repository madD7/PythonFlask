from flask import Flask

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    """
    Decorator links the return html (page) to the
    route (url) of your application.
    :return: Html Header
    """
    return '<h1>Hello Puppy!</h1>'
# End of index()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run()
