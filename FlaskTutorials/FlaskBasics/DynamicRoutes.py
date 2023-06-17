from flask import Flask

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)


"""
We may want our url extensions to be dynamic based on situation.
Eg: A Web app with many users & each of those users has a profile page.

Dynamic routes have 2 Key aspects:
    a. A Variable in the route url
    b. Parameter passed ie. value of variable
    
    Eg: route('/somePage/<name>')
    Name is passed to the decorated (linked) function. 
"""

@app.route('/')
@app.route('/home')
def index():
    """
    :return: Html Header as string
    """
    return '<h1>Hello Puppy!</h1>'
# End of index()


@app.route('/puppy/<name>')
def hello_puppy(name):
    """
    Dynamic routing example.
    :param name: input variable. Puppy name.
    :return: Html header as string with the variable value.
    """
    return '<h1>Hello {0}!<br>This is Profile page of {0}.</h1>'.format(name)
# End of hello_puppy()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run()
