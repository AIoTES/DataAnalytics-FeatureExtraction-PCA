from flask import request
from flask_restplus import Resource

from ..util.dto import PCADto
from ..service.pca_service import post_calculate_pca, post_eval_pca

api = PCADto.api
_pca_res_model = PCADto.pca_res_model
_pca_transform=PCADto.pca_transform
_pca_input=PCADto.pca_input
_pca_input_transform=PCADto.pca_input_transform

@api.route('/train')
class PCATrain(Resource):
    @api.response(200, 'PCA dimensionality reduction has been calculated.')
    @api.doc('get all user related sudoku logs',security='apikey')
    @api.expect(_pca_input, validate=True) # this line validates the input, can be commented to allow raw inputs
    def post(self):
        """read json input and calculates transformation"""
        data = request.json
        return post_calculate_pca(data=data)

@api.route('/eval')
class PCAEval(Resource):
    @api.response(200, 'Dataset dimensionality reduction has been applied.')
    @api.doc('evaluates the provided dimensionality reduction on the provided dataset')
    @api.expect(_pca_input_transform, validate=True) # this line validates the input, can be commented to allow raw inputs
    def post(self):
        """read json input and apply transformation"""
        data = request.json
        return  post_eval_pca(data=data)

        
