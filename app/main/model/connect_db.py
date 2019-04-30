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
    
