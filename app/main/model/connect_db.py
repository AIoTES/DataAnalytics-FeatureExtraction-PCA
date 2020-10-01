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
from sklearn import datasets
import pandas as pd

def eval_query(query):
    """
    function to evaluate queries to extract data
    returns: pandas' dataframe of the dataset to apply dimensinality reduction
    """
    #TODO: ADD connection with data base, check sql injections
    if (query=="test"):
        return pd.DataFrame(datasets.load_iris().data)
    else:
        pass
    
