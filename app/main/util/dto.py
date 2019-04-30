from flask_restplus import Namespace, fields

###################################################################################
#
# This script defines the Data Trasnfer Objects to be used for reponse marshalling.
#
###################################################################################

class PCADto:
    api=Namespace('pca_model',description='PCA namespace')
    pca_coef=fields.Float(description='coeficient of the array')
    pca_res_model=api.model('pca_res_model',{
        'components': fields.String(required=True, description='components serialized'),
        'explained_variance':fields.List(pca_coef,required=True,description='explained variance'),
        'explained_variance_ratio':fields.List(pca_coef,required=True,description='explained variance ratio'),
        'singular values':fields.List(pca_coef,required=True,description='explained variance ratio'),
        'n_components':fields.Integer(required=True,description='number of components'),
        'noise_variance':fields.Float(required=True,description='noise variance'),
        'model_stream':fields.String(required=True,description='model serialization')
        })
    pca_coef_list=fields.List(pca_coef,description='coeficients array')
    
    pca_transform=api.model('pca_transform',{
        'transformed_data': fields.List(pca_coef_list,required=True, description='transform data')
        })
    pca_input_stream=api.model('pca_input_stream',{
        'query':fields.String(required=False,description='query for data extraction from data lake'),
        'raw_data':fields.String(required=False,description='json serialized input stream format:{"columns":[],"index":[],"data":[[]]}'),
        })
    pca_input=api.model('pca_input',{
        'dataDesc': fields.Nested(pca_input_stream,required=True, description='#/definitions/dataDesc'),
        'options':fields.String(required=True,description='type of pca calculation to apply'),
        'n_components':fields.Integer(required=True,description='number of components'),
        'batch_size':fields.Integer(required=False,description='batch size for incremental version'),
        })
    pca_input_transform=api.model('pca_input_transform',{
        'dataDesc':fields.Nested(pca_input_stream,required=True, description='#/definitions/dataDesc'),
        'n_components':fields.Integer(required=True,description='number of components'),
        'raw_model':fields.String(required=True,description='json serialized input stream format:{"columns":[],"index":[],"data":[[]]}'),
        })
    

