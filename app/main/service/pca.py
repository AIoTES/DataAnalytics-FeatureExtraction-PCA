import logging
import numpy as np
from sklearn.decomposition import PCA, IncrementalPCA
from numpy.random import RandomState
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#Predefined pipelines, commond practice with pca is to standarise data previous to its application therefore two options are defined (raw & common practice):
transformer={'pca':Pipeline([('scaler',StandardScaler()),       # PCA with Standard Scaler
                             ('pca',PCA())]),   
             'pca_raw':Pipeline([('pca',PCA())]),               # PCA raw
             'ipca':Pipeline([('scaler',StandardScaler()),      # incremental PCA for large datasets with Standard Scaler
                             ('pca',IncrementalPCA())]),
             'ipca_raw':Pipeline([('pca',IncrementalPCA())]),   # incremental PCA raw 
            }

def train_PCA(X,n_dims,model='pca'):
    """
    name: train_PCA
    Linear dimensionality reduction using Singular Value Decomposition of the
    data to project it to a lower dimensional space.
    It uses the LAPACK implementation of the full SVD or a randomized truncated
    SVD by the method of Halko et al. 2009, depending on the shape of the input
    data and the number of components to extract.
    returns: the transformer model
    """
    estimator=transformer[model].set_params(pca__n_components=n_dims)
    estimator.fit(X)
    return estimator

def train_IPCA(X,n_dims,batch_size,model='ipca'):
    """
    name: train_IPCA
    Linear dimensionality reduction using Singular Value Decomposition of
    centered data, keeping only the most significant singular vectors to
    project the data to a lower dimensional space.
    returns: the transformer model 
    """
    estimator=transformer[model].set_params(pca__n_components=n_dims,pca__batch_size=batch_size)
    estimator.fit(X)
    return estimator

def eval_PCA(X,estimator):
    """
    name: eval_PCA
    Apply dimensionality reduction to X.
    X is projected on the first principal components previously extracted
    from a training set.
    returns: reduce set of X 
    """
    return estimator.transform(X)
