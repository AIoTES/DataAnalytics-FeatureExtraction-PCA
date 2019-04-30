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



