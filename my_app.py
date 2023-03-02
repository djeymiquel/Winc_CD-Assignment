from flask import render_template,request,url_for,redirect
from webapp import create_app

# Create a Flask app inside `app`
app = create_app()

# Assign a function to be called when the path `/` is requested
@app.route('/')
def home():
    title = "Welcome to My Space"
    return render_template('base.html', title=title)


@app.route('/home', methods=['GET', 'POST'])
def assign():
    title = "Home"
    if request.method == "POST":
        return redirect(url_for('home'))
    if request.method == "GET":
        return render_template('home.html', title=title)
    
@app.route('/assignment', methods=['GET'])
def assignment():
    title = "Assignment"
    return render_template('assignment.html', title=title)
    