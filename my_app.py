# from mylib import *
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/assignment')
def assignment():
    return 'This is my final assignment!'