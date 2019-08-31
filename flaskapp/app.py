import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def index():
    menu = ['home', 'news']
    return render_template('index.html', menu=menu)