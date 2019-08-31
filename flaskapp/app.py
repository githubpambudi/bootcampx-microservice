import os

import flask
from flask import render_template

app = flask.Flask(__name__)

import requests

DRF_HOST = os.getenv('DRF_HOST', 'localhost')
DRF_PORT = os.getenv('DRF_PORT', 5000)

ROOT_DRF = f"http://{DRF_HOST}:{DRF_PORT}"

@app.route('/')
def index():
    categories = requests.get(f'{ROOT_DRF}/api/v2/categories/')
    categories = categories.json()

    return render_template('index.html', categories=categories)
