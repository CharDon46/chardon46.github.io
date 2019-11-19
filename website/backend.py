from flask import Flask, render_template

app = Flask(__name__)

#set homepage
@app.route('/')
@app.route('/home')
def home():
    return render_template("./home1/home.html")

# projects page
@app.route('/projects/')  # be sure to include both forward slashes
def projects():
    return render_template("./projects/projects.html")

# blog page
@app.route('/blog/')  # be sure to include both forward slashes
def blog():
    return "What your you like to know about?"

#run the flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)