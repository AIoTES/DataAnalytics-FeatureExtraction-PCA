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
import pickle
import codecs
import logging
import pandas as pd

from app.main.service.pca import train_PCA,train_IPCA,eval_PCA
from app.main.model.connect_db import eval_query

###################################################################################
#
# This script defines the services to interface with the controller.
#
###################################################################################

def jsonify_numpy(data):
    return pd.DataFrame(data).to_json(orient='values')

def get_input_data(data):
    data=data['dataDesc']
    if('raw_data' in data and data['raw_data']!=None):
        X=pd.read_json(data['raw_data'])
    elif('query' in data and data['query']!=None):
        X=eval_query(data['query'])
    else:
        return None
    return X

def post_calculate_pca(data):
    """
    calculates de pca from possible data sources
    """
    X=get_input_data(data)
    if(not X.empty):
        X=X._get_numeric_data() # ensure to avoid a mixture variables problem, remember to check colinearities in encoded categorical variables before adding them to the global dataset.
        #calculate PCA
        if('options' in data and 'n_components' in data):
            comps=data['n_components']
            if( isinstance(comps, int) and comps>0 and comps<=X.shape[1]): # check if the output dimension is feasible
                if(data['options'] in ['pca','pca_raw']):
                    transf=train_PCA(X,data['n_components'],data['options'])
                    bytes_model=pickle.dumps(transf)
                    serial_model = codecs.encode(pickle.dumps(bytes_model), "base64").decode()
                    response_object = {
                        'status': 'ok',
                        'components':transf.named_steps['pca'].components_.tolist(),
                        'explained_variance':transf.named_steps['pca'].explained_variance_.tolist(),
                        'explained_variance_ratio':transf.named_steps['pca'].explained_variance_ratio_.tolist(),
                        'singular values':transf.named_steps['pca'].singular_values_.tolist(),
                        'n_components':transf.named_steps['pca'].n_components_,
                        'noise_variance':transf.named_steps['pca'].noise_variance_,
                        'model_stream':serial_model
                        }
                    print(response_object)
                    return response_object, 200
                elif(data['options'] in ['ipca','ipca_raw']):
                    logging.info(X.shape[0])
                    if(data['batch_size']>0 and data['batch_size']<=X.shape[0]): # check a logic value for batch size (stochastic and batch mode are possible)
                        transf=train_IPCA(X,data['n_components'],data['batch_size'],data['options'])
                        bytes_model=pickle.dumps(transf)
                        serial_model = codecs.encode(pickle.dumps(bytes_model), "base64").decode()
                        response_object = {
                            'status': 'ok',
                            'components':transf.named_steps['pca'].components_.tolist(),
                            'explained_variance':transf.named_steps['pca'].explained_variance_.tolist(),
                            'explained_variance_ratio':transf.named_steps['pca'].explained_variance_ratio_.tolist(),
                            'singular values':transf.named_steps['pca'].singular_values_.tolist(),
                            'n_components':transf.named_steps['pca'].n_components_,
                            'noise_variance':transf.named_steps['pca'].noise_variance_,
                            'model_stream':serial_model
                            }
                        print(response_object)
                        return response_object, 200
    response_object = {
        'status': 'fail',
        'message': 'input data required or wrong input',
    }
    return response_object, 402

def post_eval_pca(data):
    """
    Applies dimensionality reduction 
    """
    X=get_input_data(data)
    if(not X.empty):
        X=X._get_numeric_data()
        if('raw_model' in data and 'n_components' in data):
            model=pickle.loads(pickle.loads(codecs.decode(data['raw_model'].encode(), "base64")))
            #model=pickle.loads(data['raw_model'].encode('utf-8'))
            X_new=eval_PCA(X,model)
            if(isinstance(data['n_components'], int) and data['n_components']<X_new.shape[1]):
                X_new=X_new[:,0:data['n_components']]
            response_object = {
                            'status': 'ok',
                            'transformed_data':X_new.tolist()
                            }
            return response_object,200
    


        
    
    
