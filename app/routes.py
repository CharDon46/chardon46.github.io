from flask import render_template
from app import app
#set homepage
@app.route('/')
@app.route('/home')
def home():
    return render_template("./home1/home.html", title  ='Home')

# projects page
@app.route('/projects/')  # be sure to include both forward slashes
def projects():
    return render_template("./projects/projects.html")

# blog page
@app.route('/blog/')  # be sure to include both forward slashes
def blog():
    return "What would you like to know about?"