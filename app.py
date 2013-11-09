from flask import Flask

import requests
from requests.auth import HTTPBasicAuth
from flask import request, abort, g, json, redirect,session
from flask_appconfig import AppConfig

import datetime

from collections import defaultdict

import pudb

import pymongo


app = Flask(__name__)

def create_app(configfile=None):
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
#    Bootstrap(app)
    app.config.from_object('conf')

    return app



db=pymongo.MongoClient(mongo_uri).corp_ahole

from index import *

if __name__ == '__main__':
    host='0.0.0.0'
    app=create_app().run(debug=True, host=host, port=8000)