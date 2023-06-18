from flask import Flask, render_template

# Creating an app object as an instance of
# the class Flask, passing the __name__ of the module
# in which Flask is used.
app = Flask(__name__)

"""
Template inheritance:

Create a base.html file that will have a common webpage template 
that would be loaded in all other html webpages.
Common template generally has Navigation bar, footer etc.

base.html 
{% Block content %}

{% endBlock %}


other html files:
{% extends "base.html" %}
{% Block content %}

{% endBlock %}


To add url,
use in anchor tag : 

To link to a page/url, pass the python function name linked to the url path.
<a href="{{ url_for('home') }}">Puppies Website</a>

to add static file, viz. an image:
<a href="{{ url_for('static', filename='puppy_pic.jpg') }}">Click Here</a>

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


@app.route('/puppy/<name>')
def hello_puppy(name):
    """
    :param name: input variable. Puppy name.
    :return: Renderes Html header with variable from Python.
    """
    return render_template('puppy.html', puppy_name=name)
# End of hello_puppy()

if __name__ == "__main__":
    # Runs on local server Port:5000
    app.run(debug=True)
