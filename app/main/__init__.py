import os
import logging
from flask import Flask,Response
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from flask_cors import cross_origin

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)
    from flask_cors import CORS

from .config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    #TODO ADD SECRET KEY IF REQUIRED
    CORS(app)
    print('CREATING APP WITH CONFIG '+config_name)
    app.config.from_object(config_by_name[config_name])
    logging.basicConfig(level=config_by_name[config_name].LOG_LEVEL)
    return app
