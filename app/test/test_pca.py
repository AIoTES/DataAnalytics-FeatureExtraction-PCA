import os
import unittest
import logging
import pickle
import codecs
#import matplotlib.pyplot as plt

from flask import current_app
from flask_testing import TestCase

from sklearn import datasets
from app.main.service.pca import train_PCA,train_IPCA,eval_PCA


class TestTestingPCA(TestCase):
    def create_app(self):
        current_app.config.from_object('app.main.config.TestingConfig')
        return current_app
    def test_pca(self):
        logging.info("Initialising Principal Component Analysis test")
        iris = datasets.load_iris()
        X = iris.data
        logging.info("Size previous to PCA:{}".format(X.shape))
        transf=train_PCA(X,3,'pca')
        logging.info("Components calculated:\n{}".format(transf.named_steps['pca'].components_))
        logging.info("Explained variance:\n{}".format(transf.named_steps['pca'].explained_variance_))
        logging.info("Explained variance ratio:\n{}".format(transf.named_steps['pca'].explained_variance_ratio_))
        logging.info("Singular values:\n{}".format(transf.named_steps['pca'].singular_values_))
        logging.info("Number of components:\n{}".format(transf.named_steps['pca'].n_components_))
        logging.info("Noise variance:\n{}".format(transf.named_steps['pca'].noise_variance_))
        X_encoded=eval_PCA(X,transf)
        logging.info("Size subsequent to PCA:{}".format(X_encoded.shape))
        self.assertTrue(X_encoded.shape==(150,3))
        transf=train_PCA(X,3,'pca_raw')
        logging.info("Components calculated:\n{}".format(transf.named_steps['pca'].components_))
        logging.info("Explained variance:\n{}".format(transf.named_steps['pca'].explained_variance_))
        logging.info("Explained variance ratio:\n{}".format(transf.named_steps['pca'].explained_variance_ratio_))
        logging.info("Singular values:\n{}".format(transf.named_steps['pca'].singular_values_))
        logging.info("Number of components:\n{}".format(transf.named_steps['pca'].n_components_))
        logging.info("Noise variance:\n{}".format(transf.named_steps['pca'].noise_variance_))
        X_encoded=eval_PCA(X,transf)
        logging.info("Size subsequent to PCA:{}".format(X_encoded.shape))
        self.assertTrue(X_encoded.shape==(150,3))
        #logging.info(pickle.dumps(transf.named_steps['pca']))
        
    def test_serialization_deserialization(self):
        logging.info("Testing serialization of the pipeline...")
        logging.info("initialising Principal Component Analysis test")
        iris = datasets.load_iris()
        X = iris.data
        transf=train_PCA(X,3,'pca')
        logging.info("Performing serialization")
        s = pickle.dumps(transf)
        pickled = codecs.encode(pickle.dumps(s), "base64").decode()
        logging.warning(pickled)
        logging.info("Performing de-serialization")
        clf = pickle.loads(pickle.loads(codecs.decode(pickled.encode(), "base64")))
        X_encoded_2=eval_PCA(X,clf)
        logging.warning("Size subsequent to PCA:{}".format(X_encoded_2.shape))
        logging.info(s)
        self.assertTrue(X_encoded_2.shape==(150,3))
        
        
        
        
class TestTestingPCAINCREMENTAL(TestCase):
    def create_app(self):
        current_app.config.from_object('app.main.config.TestingConfig')
        return current_app
    def test_pca_incremental(self):
        logging.info("Initialising Incremental Principal Component Analysis test")
        X,_ = datasets.load_digits(return_X_y=True)
        # visualise an element of the dataset :
        #plt.gray() 
        #plt.matshow(X[12].reshape(8,8)) 
        #plt.show()
        logging.info("Size previous to PCA:{}".format(X.shape))
        transf=train_IPCA(X,5,200,'ipca')
        logging.info("Components calculated:\n{}".format(transf.named_steps['pca'].components_))
        logging.info("Explained variance:\n{}".format(transf.named_steps['pca'].explained_variance_))
        logging.info("Explained variance ratio:\n{}".format(transf.named_steps['pca'].explained_variance_ratio_))
        logging.info("Singular values:\n{}".format(transf.named_steps['pca'].singular_values_))
        logging.info("Number of components:\n{}".format(transf.named_steps['pca'].n_components_))
        logging.info("Noise variance:\n{}".format(transf.named_steps['pca'].noise_variance_))
        X_encoded=eval_PCA(X,transf)
        logging.info("Size subsequent to PCA:{}".format(X_encoded.shape))
        self.assertTrue(X_encoded.shape==(1797,5))
        transf=train_IPCA(X,5,200,'ipca_raw')
        logging.info("Components calculated:\n{}".format(transf.named_steps['pca'].components_))
        logging.info("Explained variance:\n{}".format(transf.named_steps['pca'].explained_variance_))
        logging.info("Explained variance ratio:\n{}".format(transf.named_steps['pca'].explained_variance_ratio_))
        logging.info("Singular values:\n{}".format(transf.named_steps['pca'].singular_values_))
        logging.info("Number of components:\n{}".format(transf.named_steps['pca'].n_components_))
        logging.info("Noise variance:\n{}".format(transf.named_steps['pca'].noise_variance_))
        X_encoded=eval_PCA(X,transf)
        logging.info("Size subsequent to PCA:{}".format(X_encoded.shape))
        #logging.info("Result example:\n{}".format(X_encoded))
        self.assertTrue(X_encoded.shape==(1797,5))
        
if __name__ == '__main__':
    unittest.main()
