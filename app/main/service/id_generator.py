import datetime
import random
import logging


def getnewid(model_type='pca'):
"""
name: getnewid
Generates a string to be used as model identifier
returns: a unique new identifier for the model 
"""
    id_code=""
    if(isinstance(randtoavoidcollisions,str)):
        timed_deterministic_name=str(int(datetime.datetime.now().timestamp()))
        rand_to_avoidcollisions=str(random.getrandbits(4)).zfill(2) #simple two rand numbers
        id_code='mod'+rand_to_avoidcollisions+'_'+model_type+'_'+timed_deterministic_name
    else:
        logging.error("Wrong input type for parameters in function getnewif, params info: type(model_type)=str")
        raise ValueError("Wrong input type for parameters in function getnewif, params info: type(model_type)=str")
    return id_code
