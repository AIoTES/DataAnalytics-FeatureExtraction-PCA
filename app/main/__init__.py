#
# Copyright (c) 2019 Universidad Politecnica de Madrid.
#
# This file is part of ACTIVAGE.
# See http://www.activageproject.eu/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
