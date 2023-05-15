from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/favicon.ico")
def blog():
    return render_template('charmander.jpg')


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>Hello, dogs are good!</p>"


@app.route("/about")
def about():
    return render_template('about.html')
