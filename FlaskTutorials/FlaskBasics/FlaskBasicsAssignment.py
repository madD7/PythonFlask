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
    return '<h1>Puppies are cute!</h1><br><ul>\
      <li>/info - <span>Information about this web site.</span></li>\
      <li>/puppy/puppyname - <span>Puppy profile page</span> </li>\
      <li>/puppylatin/puppyname - <span>Get Puppy name in Latin. </span></li></ul>'
# End of info()


@app.route('/puppy/<name>')
def hello_puppy(name):
    """
    Dynamic routing example.
    :param name: input variable. Puppy name.
    :return: Html header as string with the variable value.
    """
    return '<h1>Hello {0}!<br>This is Profile page of {0}.</h1>'.format(name)
# End of hello_puppy()


@app.route('/puppylatin/<name>')
def puppy_latin_name(name):
    """
    Returns puppylatin name.
    if Last character of puppy name is not 'y', add 'y' to name.
    If last character of puppy name is 'y', replace it with 'iful'.
    :param name: Puppy name
    :return: Html header with PuppyLatin name, as string.
    """
    if name[-1] != 'y':
        newname = name + 'y'
    else:
        newname = name[:-1] + 'iful'

    return '<h1>Hi {}. Your PuppyLatin name is {}</h1>'.format(name, newname)
# End of puppy_latin()


if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run()
