from flask import Flask, render_template

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)

"""
Flask will look for html files in the 'templates' directory.
We can render html templates by importing the render template function
from flask and returning that html file from associated function.

Static files, like image files, are stored in the static folder. 
The files of the static folder are linked in the html file.
"""


@app.route('/')
@app.route('/home')
def index():
    """
    Flask will automatically look in the same level directory for a folder
    named 'templates', and then it's going to look inside that templates folder
    for a file name 'basic.html'.
    The puppy pic is rendered from the static folder, in the basic.html file.
    :return: Rendered Html page
    """
    return render_template('basic.html') # Must match exactly with the filename
# End of index()


@app.route('/puppy/<name>')
def hello_puppy(name):
    """
    Dynamic routing example.
    Jinja templating lets us insert variables from our python
    code to the html file. use {{<var_name>}} in the html file.
    And pass the variable in the render template funtion
    using syntax:
    var_name_in_html = my_variable_to_pass.

    often, we use same variable names for ease of read.
    But, in this example, we demonstrate using different names.

    :param name: input variable. Puppy name.
    :return: Renderes Html header with variable from Python.
    """
    return render_template('puppy_name.html', puppy_name=name)
# End of hello_puppy()


@app.route('/puppy/ownerinfo')
def owner_info():
    """
    Demonstrate passing a list
    :param name: input variable. Puppy name.
    :return: Html header as string with the variable value.
    """
    owner_details = ['PuppyName','FirstName', 'LastName', 12345]
    owner_dict = {'Address': 'House 1, Random Street, Some City, DreamLand',
                  'Contact': 123456789}
    return render_template('static_owner_info.html',
                           owner_details=owner_details,
                           owner_dict=owner_dict)
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
    app.run()
