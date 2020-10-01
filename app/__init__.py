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
# app/__init__.py
import os
from flask_restplus import Api
from flask import Blueprint
from flask_cors import CORS
from flask import url_for

class MyApi(Api):
    @property
    def specs_url(self):
        """Patch for showing documentation over HTTPS"""
        scheme = os.getenv('API_PROTOCOL','https')
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


from .main.controller.pca_controller import api as pca_ns


blueprint = Blueprint('api', __name__)
CORS(blueprint)
authorizations = {
    'apikey': {
        'type' : 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = MyApi(blueprint,
          authorizations=authorizations,
          doc='/docs/',
          title='ACTIVAGE PCA WEB SERVICE',
          version='1.0',
          description='TODO: ADD DESCRIPTION OF THE SERVICES'
          )

api.add_namespace(pca_ns, path='/pca')



