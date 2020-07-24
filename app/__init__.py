from flask import Flask, request, session, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

import json, logging, os


app = Flask(__name__)
logging.basicConfig(filename='/var/log/flask.log', level=logging.INFO)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Define Tables here

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
