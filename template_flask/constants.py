REQUIREMENTS = [
    'flask',
    'flask_sqlalchemy',
    'flask_login',
    'flask_mail',
    'flask_wtf',
    'flask_debugtoolbar',
    'pytest',
    'pytest_cov'
]

INDEX_HTML = {
    1: ['<!DOCTYPE html>', False],
    2: ['<html lang="en">', False],
    3: ['<head>', False],
    4: ['\t<meta charset="UTF-8">', False],
    5: ['\t<title>NEW PROJECT: {app}</title>', True],
    6: ['</head>', False],
    7: ['<body>', False],
    8: ['\t<h1>Welcome to your new project: {app}</h1>', True],
    9: ['</body>', False],
    10: ['</html>', False]
}

CONFIG_INIT = {
    1: ["", False]
}

CONFIG_CONFIG = {
    1: ['SECRET_KEY = """{secret_key}"""', True],
    2: ["SQLALCHEMY_DATABASE_URI = 'sqlite:///{app}_db.db'", False],
    3: ["# SQLALCHEMY_DATABASE_URI = 'postgresql://<your_username>:<your_password>@<host>:<port>/<database_name>'", False],
    4: ["# SQLALCHEMY_DATABASE_URI = 'mysql://<your_username>:<your_password>@<host>:<port>/<database_name>", False],
    5: ["# SQLALCHEMY_DATABASE_URI = 'oracle://<your_username>:<your_password>@<host>:<port>/<sid_name>", False]
}

ROUTE_INIT = {
    1: ["", False]
}

ROUTE_ROUTE = {
    1: ["from flask import render_template, redirect, url_for, request, session, flash", False],
    2: ["from {app}_app import app, db, Model", True],
    3: ["", False],
    4: ["", False],
    5: ["@app.route('/', methods=['POST', 'GET'])", False],
    6: ["@app.route('/home', methods=['POST', 'GET'])", False],
    7: ["def index():", False],
    8: ["\tif request.method == 'POST':", False],
    9: ["\t\tprint(request.form)", False],
    10: ["\t\tprint(request.files)", False],
    11: ["\treturn render_template('index.html')", False]
}

MODEL_INIT = {
    1: ["# IMPORT ALL MODELS AND DB TO HERE AND THEN THE MAIN __INIT__.PY WILL", False],
    2: ["# IMPORT * FROM HERE", False],
    3: ["", False],
    4: ["from {app}_app.models.db import db", True],
    5: ["from {app}_app.models.model import Model", True]
}

MODEL_DB = {
    1: ["from flask_sqlalchemy import SQLAlchemy", False],
    2: ["", False],
    3: ["# SHARED DATABASE FOR MODELS IN SEPARATE .PY FILES.", False],
    4: ["# MODELS.__INIT__.PY IMPORTS DB (AS WELL AS OTHER MODELS) AND", False],
    5: ["# THEN THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY.", False],
    6: ["", False],
    7: ["db = SQLAlchemy()", False]
}

MODEL_MODEL = {
    1: ["from datetime import datetime", False],
    2: ["from {app}_app import db", True],
    3: ["", False],
    4: ["", False],
    5: ["# CREATE CUSTOM MODEL HERE", False],
    6: ["# IF CREATING MORE MODELS IN SEPARATE .PY FILES GO TO MODELS.__INIT__.PY AND IMPORT THE NEW MODEL", False],
    7: ["# THE MAIN __INIT__.PY FOR THE APP WILL IMPORT * FROM MODELS.__INIT__.PY", False],
    8: ["", False],
    9: ["class Model(db.Model):", False],
    10: ["\tid = db.Column(db.Integer, primary_key=True)", False]
}

RUN = {
    1: ["from {app}_app import app", True],
    2: ["", False],
    3: ["", False],
    4: ["if __name__ == '__main__':", False],
    5: ["\tapp.run(debug=True)", False]
}

INIT = {
    1: ["from flask import Flask", False],
    2: ["# from flask_login import ()", False],
    3: ["# from flask_mail import ()", False],
    4: ["# from flask_wft import ()", False],
    5: ["# from flask_debugtoolbar import ()", False],
    6: ["from {app}_app.config import *", True],
    7: ["from {app}_app.models import *", True],
    8: ["", False],
    9: ["", False],
    10: ["app = Flask(__name__)", False],
    11: ["app.config['SECRET_KEY'] = SECRET_KEY", False],
    12: ["app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI", False],
    13: ["app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False", False],
    14: ["# app.config[''] = ''", False],
    15: ["# app.config[''] = ''", False],
    16: ["# app.config[''] = ''", False],
    17: ["# app.config[''] = ''", False],
    18: ["", False],
    19: ["with app.app_context():", False],
    20: ["\tdb.init_app(app)", False],
    21: ["\tdb.create_all()", False],
    22: ["", False],
    23: ["from {app}_app.routes import routes", True]
}

