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
    
# Debugger - debug=True
When enabling the debugger, a pin is printed (Eg: * Debugger PIN: 710-168-029) 
    in the console where the script was executed. 
You can copy the pin and paste in the WebPage Browser, 
    when you click the console icon at the right corner of the error string 
    to connect to the debugger console. 
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


@app.route('/fault/<name>')
def debug_error(name):
    """
    To understand debugging.
    The web page displays the Error with the Traceback.
    :param name:
    :return: Returns the 100th character of the name variable value,
                basically generates an 'string out of range' error.
    """
    return '<h1>100th Letter of the Name is {}</h1>'.format(name[100])
# End of debug_error()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run(debug=True)
