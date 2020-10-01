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
