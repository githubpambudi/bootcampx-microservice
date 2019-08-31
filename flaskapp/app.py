import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__ ':
    app.run(host = '0.0.0.0')

@app.route('/')
def index():
    menu = ['home', 'news']
    return render_template('index.html', menu=menu)